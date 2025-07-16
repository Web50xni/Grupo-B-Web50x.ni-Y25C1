from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, StudyspaceForm
from django.contrib import messages
from django.urls import reverse

def home_view(request):

    return render(request, 'home.html', {
        "studyspaces":studyspaces.keys()
    })


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'auth/logout.html')


def studyspace_view(request, title):
    """
    Esta funcion recibe como parametro desde la URL un title, con el fin de renderizar una pagina
    en especifico para ese studyspace que coincida con ese title, en caso de no coincidir, se redirecciona 
    al usuario a la vista para crear un nuevo studyspace.
     """

    #validamos que title exista como una key dentro de studyspaces
    if not title in studyspaces.keys():
        return create_studyspace_view(request)

    #renderizamos la template y pasamos studyspace como contexto
    studyspace = studyspaces[title]
    return render(request, "studyspace.html", {
        "studyspace": studyspace,
    })


def create_studyspace_view(request):
    """
    La funcion create_studyspace_view, renderiza una template con el formulario StudyspaceForm(), si el metodo http
    de la request es post, entonces la funcion crea una instancia de nuestra clase StudyspaceForm(), y los campos de esta
    se llenan con request.POST, que vendria siendo la data que el usuario esta enviando desde el form en create.html.
    """
    if request.method == "POST":
        #instanciamos nuestra funcion y construimos el objeto con request.POST
        form = StudyspaceForm(request.POST)
        #validamos que la data sea correcta
        if form.is_valid():
            #extraemos el title del studyspace del diccionario cleaned_data
            title = form.cleaned_data["title"]
            #agregamos el nuevo studyspace a studyspaces
            studyspaces.update({
                title:form.cleaned_data
            })
            #redireccionamos a la pagina del nuevo studyspace
            return redirect(reverse("studyspace", kwargs={
                "title": title
            }))
    #renderizamos create.html con el formulario StudyspaceForm()
    return render(request, "create.html", {
        "form": StudyspaceForm()
    })

#nuestro dic para los studyspaces, las keys son los titulos de cada studyspace, y los valores, 
# son otro dic que contiene toda la data.
studyspaces = {
    "Django": {
        "title": "Django",
        "description": "Este es mi espacio de estudio para Django.",
        "goal": "Aprender Django para crear paginas dinamicas.",
    },
}