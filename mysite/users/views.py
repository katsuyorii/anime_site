from typing import Any
from django.db import models
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm, UserRegistrationForm, ProfileUserForm
from django.urls import reverse_lazy
from .models import User


class LoginUserView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


class RegistrationUserView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'

    def get_success_url(self):
        return reverse_lazy('index')


class ProfileUserView(UpdateView):
    model = User
    form_class = ProfileUserForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def get_object(self):
        return self.request.user
