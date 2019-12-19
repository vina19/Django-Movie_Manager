from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from movie_manager import settings

# https://stackoverflow.com/questions/53461410/make-user-email-unique-django
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class Movie(models.Model):
    name = models.CharField(max_length=300)
    year = models.CharField(max_length=5)
    plot = models.CharField(max_length=1500)
    imdb_rating = models.FloatField(default=0.0)
    poster = models.ImageField(upload_to='movie_posters/', blank=True, null=True)
    favorite = models.BooleanField(default=False)
    watched = models.BooleanField(default=False)
    trailer = models.CharField(max_length=150, default=None, null=True, blank=True)

    def __str__(self):
        poster_str = self.poster.url if self.poster else 'no poster'
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    favorite_movie = models.ForeignKey(Movie, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '{} Profile'.format(self.user)