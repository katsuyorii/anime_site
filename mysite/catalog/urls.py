from django.urls import path
from .views import IndexView, AnimeListView, AnimeDetailView, CommentDeleteView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('anime', AnimeListView.as_view(), name='anime_list'),
    path('anime/<slug:anime_slug>', AnimeDetailView.as_view(), name='anime_detail'),
    path('comment-delete/<slug:comm_slug>', CommentDeleteView.as_view(), name='comm_delete'),
]
