from django.views.generic import ListView
from .models import Anime


class IndexView(ListView):
    model = Anime
    template_name = 'catalog/index.html'
    context_object_name = 'anime_list'

    def get_queryset(self):
        queryset = {
            'top_anime': Anime.objects.all()[:5],
            'last_anime': Anime.objects.order_by('-create_date')[:5],
        }

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'AnimeOne'

        return context


class AnimeListView(ListView):
    model = Anime
    template_name = 'catalog/anime.html'
    context_object_name = 'anime_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог аниме'

        return context
