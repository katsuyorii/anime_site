from django.contrib import admin
from .models import Genre, Anime, AnimeShots, Comment

admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(AnimeShots)
admin.site.register(Comment)
