from django.contrib import admin
from .models import Movie, UserProfile

# Register your models here.
admin.site.register(Movie)
admin.site.register(UserProfile)