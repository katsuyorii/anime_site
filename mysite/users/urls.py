from django.urls import path
from .views import LoginUserView, RegistrationUserView, ProfileUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('registration/', RegistrationUserView.as_view(), name='registration'),
    path('profile', ProfileUserView.as_view(), name='profile'),
]
