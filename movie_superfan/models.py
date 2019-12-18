from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from movie_manager import settings

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

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

class Comment(models.Model):
    movie_title = models.ForeignKey(Movie, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField(max_length=500, blank=False)
    posted_date = models.DateTimeField(blank=False)

    def date_publish(self):
        date = datetime.datetime.today()
        self.save()

    def __str__(self):
        return 'Comment from user ID {} for movie {}'.format(self.user, self.movie_title)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return '{} Profile'.format(self.user)