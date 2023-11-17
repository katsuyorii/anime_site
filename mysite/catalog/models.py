from django.db import models
from django.urls import reverse
from transliterate import slugify
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(verbose_name='Наименование жанра аниме', max_length=200)
    slug = models.SlugField(verbose_name='Слаг', max_length=200, db_index=True, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, 'ru')
        super().save()

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Anime(models.Model):
    class Age(models.TextChoices):
        AGE_G = 'g', 'G'
        AGE_PG = 'pg', 'PG'
        AGE_PG13 = 'pg13', 'PG-13'
        AGE_R = 'r', 'R'
        AGE_NC17 = 'nc17', 'NC-17'

    class Status(models.TextChoices):
        ONG = 'on', 'Онгоинг'
        OUT = 'out', 'Вышел'
        AN = 'an', 'Анонс'

    class Type(models.TextChoices):
        SERIAL = 'sr', 'Сериал'
        FILM = 'fl', 'Фильм'

    title = models.CharField(verbose_name='Наименование аниме', max_length=200)
    title_eng = models.CharField(verbose_name='Наименование аниме по англ.', max_length=200)
    slug = models.SlugField(verbose_name='Слаг', max_length=200, db_index=True, unique=True, null=True, blank=True)
    type = models.CharField(verbose_name='Тип аниме', max_length=2, choices=Type.choices)
    episodes = models.PositiveSmallIntegerField(verbose_name='Количество серий в сезоне', null=True, blank=True)
    status = models.CharField(verbose_name='Статус аниме', max_length=3, choices=Status.choices)
    genres = models.ManyToManyField(to=Genre, verbose_name='Жанры аниме', db_index=True)
    studia = models.CharField(verbose_name='Студия', max_length=200, null=True, blank=True)
    age_restrictions = models.CharField(verbose_name='Возрастное ограничение', max_length=4, choices=Age.choices)
    year = models.PositiveIntegerField(verbose_name='Год выпуска аниме')
    create_date = models.DateTimeField(verbose_name='Дата добавления аниме', auto_now_add=True)
    description_full = models.TextField(verbose_name='Полное описание аниме')
    description_partial = models.CharField(verbose_name='Краткое описание аниме', max_length=300)
    poster_image = models.ImageField(verbose_name='Изображение постера аниме', upload_to='posters/')
    duration = models.CharField(verbose_name='Длительность', max_length=200, null=True, blank=True, help_text='Поле для аниме-фильмов')
    author = models.CharField(verbose_name='Автор', max_length=200, null=True, blank=True, help_text='Поле для аниме-фильмов')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, 'ru')
        super().save()

    def get_absolute_url(self):
        return reverse("anime_detail", kwargs={"anime_slug": self.slug})

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'


class AnimeShots(models.Model):
    image = models.ImageField(verbose_name='Изображение постера аниме', upload_to='anime-shorts/')
    anime = models.ForeignKey(verbose_name='Аниме', to=Anime, on_delete=models.CASCADE)

    def __str__(self):
        return f'Кадр из аниме - {self.anime.title}'

    class Meta:
        verbose_name = 'Кадр из аниме'
        verbose_name_plural = 'Кадры из аниме'


class Comment(models.Model):
    anime = models.ForeignKey(verbose_name='Аниме', to=Anime, on_delete=models.CASCADE)
    author = models.ForeignKey(verbose_name='Автор', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Текст комментария')
    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    slug = models.SlugField(verbose_name='Слаг', max_length=200, db_index=True, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.content + str(self.author.pk), 'ru')
        super().save()

    def __str__(self):
        return f'{self.author.username} | {self.anime.title}'

    def get_absolute_url(self):
        return reverse("comm_delete", kwargs={"comm_slug": self.slug})

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
