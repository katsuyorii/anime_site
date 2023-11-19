from django.urls import path
from .views import LoginUserView, RegistrationUserView, ProfileUserView, logout_user, UserAnimeList, UserAnimeListDelete

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('registration/', RegistrationUserView.as_view(), name='registration'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
    path('profile/logout', logout_user, name='logout'),
    path('profile/my_anime_list', UserAnimeList.as_view(), name='my_anime_list'),
    path('profile/my_anime_list/delete-from-list/<int:pk>', UserAnimeListDelete.as_view(), name='my_anime_list_delete'),
]
