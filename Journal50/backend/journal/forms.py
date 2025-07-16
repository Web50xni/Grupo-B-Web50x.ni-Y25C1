from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo electrónico')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class StudyspaceForm(forms.Form):
    title = forms.CharField(required=True, label="Titulo")
    #widget nos permite modificar como se mostrara el CharField, en este caso, como un textarea
    description = forms.CharField(required=False, label="Descripcion", widget=forms.Textarea)
    goal = forms.CharField(required=False, label="Meta")