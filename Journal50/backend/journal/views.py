from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, StudyspaceForm
from django.contrib import messages
from django.urls import reverse
from .utils import build_note_dict

def home_view(request):
    return render(request, 'home.html')


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


def studyspace_list_view(request):
    return render(request, "studyspace_list.html", {
        "studyspaces":studyspaces.keys()
    })


def studyspace_detail_view(request, title):
    """
    Esta funcion recibe como parametro desde la URL un title, con el fin de renderizar una pagina
    en especifico para ese studyspace que coincida con ese title, en caso de no coincidir, se redirecciona 
    al usuario a la vista para crear un nuevo studyspace.
     """

    #validamos que title exista como una key dentro de studyspaces
    if not title in studyspaces.keys():
        return redirect(reverse("studyspace_create"))

    #renderizamos la template y pasamos studyspace como contexto
    studyspace = studyspaces[title]
    return render(request, "studyspace_detail.html", {
        "studyspace": studyspace,
        #creamos una lista a comprensión que contenga los titulos de las notes que tienen en el campo "studyspace"
        #el valor del title que recibe esta funcion como parametro
        "notes": [note.get("title", {}) for note in notes.values() if note["studyspace"] == title]
    })


def studyspace_create_view(request):
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
            return redirect(reverse("studyspace_detail", kwargs={
                "title": title
            }))
    #renderizamos create.html con el formulario StudyspaceForm()
    return render(request, "studyspace_create.html", {
        "form": StudyspaceForm()
    })


def studyspace_update_view(request, title):
    if not title in studyspaces.keys():
        return redirect('home')
    
    if request.method == "POST":
        form = StudyspaceForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title", {})
            studyspaces.update({
                title:form.cleaned_data
            })
            return redirect(reverse("studyspace_detail", kwargs={
                "title":title
            }))
        else:
            return redirect('home')
    studyspace = studyspaces[title]
    #la propiedad initial de un Form nos permite renderizar el formulario con los campos
    #teniendo un valor inicial
    return render(request, 'studyspace_update.html', {
        'form' : StudyspaceForm(initial=studyspace),
        'title' : studyspace["title"]
    })
    

def studyspace_delete_view(request, title):
    if request.method == "POST":
        if title in studyspaces:
            del studyspaces[title]
        return redirect(reverse("studyspace_list"))
    #tambien es posible pasar funciones como contexto 
    #a nuestras plantillas, en este caso, se pasa la funcion reverse()
    return render(request, "studyspace_delete.html", {
      "obj_name" : "studyspace",
      "obj_title" : title,
      "cancelar" : reverse("studyspace_detail", kwargs={'title' : title})
    })


def note_detail_view(request, title, studyspace):

    note = notes.get(title, {}) 
    if studyspace == note.get("studyspace", {}):

        return render(request, "note_detail.html", {
            "note": note
        })

    return redirect("studyspace_list")


#nuestro dic para los studyspaces, las keys son los titulos de cada studyspace, y los valores, 
# son otro dic que contiene toda la data.
studyspaces = {
    "Django": {
        "title": "Django",
        "description": "Este es mi espacio de estudio para Django.",
        "goal": "Aprender Django para crear páginas dinámicas.",
    },
}

notes = {
    "Modelos En Django": {
        "title":"Modelos En Django",
        "studyspace": "Django",
        "content": "En Django, un modelo es una representación de la estructura de datos de tu aplicación en la base de datos. Se define como una clase Python que hereda de django.db.models.Model. Cada atributo de la clase modelo representa un campo en la tabla de la base de datos.",
        "links": ["https://www.youtube.com/watch?v=YzP164YANAU", "https://docs.djangoproject.com/es/5.2/topics/db/models/"],
        "code": {
            "language": "python",
            "source": "from django.db import models \n\n#Modelo Person representa una tabla en la BD \nclass Person(models.Model): \n    first_name = models.CharField(max_length=30) \n    last_name = models.CharField(max_length=30)",
        },
        "created_at": "18/07/25",
    }
}