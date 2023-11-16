from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm, UserRegistrationForm
from django.urls import reverse_lazy


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
