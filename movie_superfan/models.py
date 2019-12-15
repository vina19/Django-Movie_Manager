from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create Movie model
class Movie(models.Model):
    name = models.CharField(max_length=300)
    year = models.CharField(max_length=5)
    plot = models.CharField(max_length=1500)
    imdb_rating = models.FloatField(default=0.0)
    poster = models.ImageField(upload_to='movie_posters/', blank=True, null=True)
    watched = models.BooleanField(default=False)
    trailer = models.CharField(max_length=150, default=None, null=True, blank=True)

    def __str__(self):
        poster_str = self.poster.url if self.poster else 'no poster'
        return self.name

class HighestRevenueMovie(models.Model):
    name = models.CharField(max_length=300)
    revenue = models.IntegerField()

    def __str__(self):
        return self.name
