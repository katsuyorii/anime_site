from django.views.generic import ListView, DetailView
from .models import Anime, AnimeShots, Comment
from django.views.generic.edit import FormMixin
from .forms import AddCommentForm
from django.urls import reverse_lazy


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
    paginate_by = 3

    def get_queryset(self):
        queryset = Anime.objects.all().prefetch_related('genres')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог аниме'

        return context


class AnimeDetailView(FormMixin, DetailView):
    model = Anime
    template_name = 'catalog/anime-detail.html'
    context_object_name = 'anime'
    slug_url_kwarg = 'anime_slug'
    form_class = AddCommentForm

    def get_success_url(self):
        return reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['anime_shorts'] = AnimeShots.objects.filter(anime_id=self.object.pk)
        context['comments'] = Comment.objects.filter(anime_id=self.object.pk).select_related('author', 'anime')
        context['form'] = self.get_form()

        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            comm = form.save(commit=False)
            current_anime = self.get_object()
            comm.anime_id = current_anime.pk
            comm.author_id = request.user.pk
            comm.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
