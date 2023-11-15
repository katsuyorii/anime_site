from django.urls import path
from .views import IndexView, AnimeListView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('anime/', AnimeListView.as_view(), name='anime_list'),
]
