from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, ListView ,DeleteView
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm, UserRegistrationForm, ProfileUserForm
from django.urls import reverse_lazy
from .models import User, UserAnimeWatchPlanned
from django.contrib.auth import logout


class LoginUserView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


class RegistrationUserView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'

    def get_success_url(self):
        return reverse_lazy('profile')


class ProfileUserView(UpdateView):
    model = User
    form_class = ProfileUserForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('index')

    # Переопределяем метод, чтобы не вызывать доп. запрос в БД, а также чтобы не искать по slug или pk.
    def get_object(self):
        return self.request.user


def logout_user(request):
    logout(request)
    return redirect('index')


class UserAnimeList(ListView):
    model = UserAnimeWatchPlanned
    template_name = 'users/my_anime.html'
    context_object_name = 'user_anime_list'

    def get_queryset(self):
        queryset = UserAnimeWatchPlanned.objects.filter(user_id=self.request.user.pk).select_related('anime')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Список аниме пользователя {self.request.user.username}'

        return context


class UserAnimeListDelete(DeleteView):
    model = UserAnimeWatchPlanned
    template_name = 'users/delete-confirm.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'anime'

    def get_success_url(self):
        return reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление аниме из списка'

        return context
