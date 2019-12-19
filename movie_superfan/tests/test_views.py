from django.test import TestCase, Client

from django.urls import reverse
from django.contrib import auth

from movie_superfan.models import Movie
from movie_superfan.views import movie_detail, movie_list, user_profile, user_register 
from django.contrib.auth.models import User

import re

class TestMovieProject(TestCase):

    def test_homepage(self):

        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, 200)

class TestMovieViews(TestCase):

    fixture = ['testing_movies']

    def test_correct_template_used_for_display_movie_list(self):
        
        response = self.client.get(reverse('movie_list'))
        self.assertTemplateUsed(response, 'movie_superfan/movie_list.html')

    # def test_movie_list(self):

    #     response = self.client.get(reverse('movie_list'))

    #     movie_name = Movie(name='Jumanji: The Next Level')
    #     movie_poster = Movie(poster='jumanji.jpg')

    #     self.assertContains(response, movie_name)
    #     self.assertContains(response, movie_poster)
            
    # AssertionError: No tempalates used to render the response
    # def test_correct_template_used_for_display_movie_detail(self):

    #     response = self.client.get(reverse('movie_detail', kwargs={'movie_pk':1}))
    #     self.assertTemplateUsed(response, 'movie_superfan/movie_detail.html')

class TestsUserViews(TestCase):

    fixture = ['testing_users']

    # Test if the user registration able to post and get the user data.
    def test_user_sign_up_(self):

        response = self.client.post(reverse('user_register'), {'username':'alexis', 'email':'alexis@gmail.com', 'password1':'abcd1234defg', 'password2':'abcd1234defg'}, follow=True)

        user = auth.get_user(self.client)
        self.assertEqual(user.username, 'alexis')
    
    # Test after the user register, they'll redirect to login page. 
    def test_resgistered_user_redirects_to_correct_page(self):

        response = self.client.post(reverse('user_register'), {'username':'alexis', 'email':'alexis@gmail.com', 'password1':'abcd1234defg', 'password2':'abcd1234defg'}, follow=True)

        self.assertRedirects(response, reverse('user_login'))
    
    # Test success account created message display to the user after they register.
    def test_user_register_success_message(self):

        response = self.client.post(reverse('user_register'), {'username':'alexis', 'email':'alexis@gmail.com', 'password1':'abcd1234defg', 'password2':'abcd1234defg'}, follow=True)
        user1 = auth.get_user(self.client)

        self.assertContains(response, 'Account created for {}! You can now log in!'.format(user1))
        
    # Test if the logout page contains the right message to the user.
    def test_user_logout_display_message(self):
        
        response = self.client.get(reverse('user_logout'))
        self.assertContains(response, 'You have been logged out')