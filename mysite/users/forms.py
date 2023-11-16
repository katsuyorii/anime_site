from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Логин",
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': "Пароль",
    }))

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Логин",
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': "Пароль",
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': "Повторите пароль",
    }))

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]


class ProfileUserForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Имя",
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Логин",
        'readonly': True,
    }))

    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Фамилия",
    }))

    email = forms.CharField(required=False, widget=forms.EmailInput(attrs={
        'class': "form-control",
        'placeholder': "E-mail",
    }))

    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': "form-control",
    }))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'image',
        ]