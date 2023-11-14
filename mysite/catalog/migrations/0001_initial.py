# Generated by Django 4.2.7 on 2023-11-14 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование жанра аниме')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Наименование аниме')),
                ('title_eng', models.CharField(max_length=200, verbose_name='Наименование аниме по англ.')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='Слаг')),
                ('type', models.CharField(choices=[('sr', 'Сериал'), ('fl', 'Фильм')], max_length=2, verbose_name='Тип аниме')),
                ('episodes', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество серий в сезоне')),
                ('status', models.CharField(choices=[('on', 'Онгоинг'), ('out', 'Вышел'), ('an', 'Анонс')], max_length=3, verbose_name='Статус аниме')),
                ('studia', models.CharField(max_length=200, verbose_name='Студия')),
                ('age_restrictions', models.CharField(choices=[('g', 'G'), ('pg', 'PG'), ('pg13', 'PG-13'), ('r', 'R'), ('nc17', 'NC-17')], max_length=4, verbose_name='Возрастное ограничение')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска аниме')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления аниме')),
                ('description_full', models.TextField(verbose_name='Полное описание аниме')),
                ('description_partial', models.CharField(max_length=300, verbose_name='Краткое описание аниме')),
                ('poster_image', models.ImageField(upload_to='posters/', verbose_name='Изображение постера аниме')),
                ('genres', models.ManyToManyField(db_index=True, related_name='genres_anime', to='catalog.genre', verbose_name='Жанры аниме')),
            ],
            options={
                'verbose_name': 'Аниме',
                'verbose_name_plural': 'Аниме',
            },
        ),
    ]
