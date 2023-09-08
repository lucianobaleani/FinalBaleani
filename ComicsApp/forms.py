from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ComicsApp.models import Comic, ChatBox, Avatar, Cover


class ComicForm(forms.Form):
    class Meta:
        model = Comic
        fields = ("user", "name", "editorial", "author", "published_year")

    name = forms.CharField(max_length=70)
    editorial = forms.CharField(max_length=70)
    author = forms.CharField(max_length=70)
    published_year = forms.IntegerField()
    widgets = {
        "user": forms.TextInput(
            attrs={
                "class": "form-control",
                "value": "",
                "id": "user_id",
                "type": "hidden",
            }
        )
    }


class CoverForm(forms.Form):
    cover = forms.ImageField(label="Cover")


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {campo: "" for campo in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar Contraseña", widget=forms.PasswordInput
    )
    first_name = forms.CharField(label="Modificar Nombre")
    last_name = forms.CharField(label="Modificar Apellido")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}


class AvatarForm(forms.Form):
    image = forms.ImageField(label="Avatar")
