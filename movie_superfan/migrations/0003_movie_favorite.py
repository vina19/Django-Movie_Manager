# Generated by Django 2.1.11 on 2019-12-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_superfan', '0002_auto_20191218_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
