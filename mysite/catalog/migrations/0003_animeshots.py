# Generated by Django 4.2.7 on 2023-11-15 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_anime_author_anime_duration_alter_anime_studia'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='anime-shorts/', verbose_name='Изображение постера аниме')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.anime', verbose_name='Аниме')),
            ],
            options={
                'verbose_name': 'Кадр из аниме',
                'verbose_name_plural': 'Кадры из аниме',
            },
        ),
    ]
