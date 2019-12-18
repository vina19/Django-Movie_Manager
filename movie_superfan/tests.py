from django.test import TestCase, Client

from django.urls import reverse
from django.contrib import auth

from .models import Movie
from .views import movie_detail, movie_list, user_profile, user_register 
from django.contrib.auth.models import User

import re

class MovieModelTest(TestCase):

    def test_string_title(self):
        movie_name = Movie(name='Parasit')
        self.assertEqual(str(movie_name), movie_name.name)

class MovieProjectTest(TestCase):

    def test_homepage(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, 200)

class TestsMovieViews(TestCase):

    fixture = ['testing_movies']

    def test_correct_template_used_for_display_movie_list(self):
        
        response = self.client.get(reverse('movie_list'))
        self.assertTemplateUsed(response, 'movie_superfan/movie_list.html')

    # def test_correct_template_used_for_display_movie_detail(self):

    #     response = self.client.get(reverse('movie_detail', kwargs={'movie_pk':1}))
    #     self.assertTemplateUsed(response, 'movie_superfan/movie_detail.html')

class TestsUserViews(TestCase):

    fixture = ['testing_users']

    def test_user_logout_display(self):
        
        response = self.client.get(reverse('user_logout'))
        self.assertContains(response, 'You have been logged out')

    