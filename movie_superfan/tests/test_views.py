from django.test import TestCase, Client

from django.urls import reverse
from django.contrib import auth

from movie_superfan.models import Movie
from django.contrib.auth.models import User

import re

class TestMovieViews(TestCase):

    fixture = ['testing_movies']

    def test_correct_template_used_for_display_movie_list(self):
        response = self.client.get(reverse('movie_superfan:movie_list'))
        self.assertTemplateUsed(response, 'movie_superfan/movie_list.html')

    def test_correct_tempalate_used_for_display_movie_detail(self):
        response = self.client.get(reverse('movie_superfan:movie_detail'))
        self.assertTemplateUsed(response, 'movie_superfan/movie_detail.html')
    
