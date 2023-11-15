from django.contrib import admin
from .models import Genre, Anime, AnimeShots

admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(AnimeShots)
