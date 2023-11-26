# Generated by Django 4.2.7 on 2023-11-26 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_useranimewatchplanned_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranimewatchplanned',
            name='status',
            field=models.CharField(choices=[('', '-------'), ('wa', 'Просмотрено'), ('zp', 'Запланировано')], max_length=2, verbose_name='Статус аниме'),
        ),
    ]