from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Studyspaces

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo electrónico')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class StudyspaceShareForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Studyspaces
        fields = ['users']





        
'''
    #Usamos el constructor para personalizar nuestro formulario, en este caso, agregando clases de bootstrap
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

'''
'''class StudyspaceForm(forms.Form):
    title = forms.CharField(required=True, label="Título")
    #widget nos permite modificar como se mostrara el CharField, en este caso, como un textarea
    description = forms.CharField(required=False, label="Descripción", widget=forms.Textarea)
    goal = forms.CharField(required=False, label="Meta")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class NoteForm(forms.Form):
    title = forms.CharField(required=True, label="Título")
    content = forms.CharField(required=False, label="Contenido", widget=forms.Textarea)

    links = forms.CharField(required=False, label="Enlaces (Cada uno separado por un espacio)", widget=forms.Textarea)

    language = forms.CharField(required=False, label='Languaje')
    source = forms.CharField(required=False, widget=forms.Textarea, label="Codigo")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            '''