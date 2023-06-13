from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginAgenteForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Usuario",
                "class": "form-control input-lg"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control input-lg"
            }
        ))

class LoginBeneficiarioForm(forms.Form):
    username = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Documento",
                "class": "form-control input-lg"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control input-lg"
            }
        ))

class SignUpAgenteForm(UserCreationForm):
    password2 = None
    email = None

    class Meta:
        model = User
        fields = ('username', 'password1')

class SignUpBeneficiarioForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Documento",
                "class": "form-control input-lg"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control input-lg"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control input-lg"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repetir contraseña",
                "class": "form-control input-lg"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
