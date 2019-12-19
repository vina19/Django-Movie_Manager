from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError
from movie_superfan.models import Movie, CustomUser

# Test the string for displaying the movie
class TestMovieModel(TestCase):

    def test_str_movie_title(self):

        movie_name = Movie(name='Parasit')
        self.assertEqual(str(movie_name), movie_name.name)

# Test that Custom User Model displaying the error message if the user trying to create duplicate username and email
class TestCustomUserModel(TestCase):

    def test_avoid_duplicate_username(self):

        user1 = CustomUser(username='najef', email='najef@gmail.com')
        user1.save()

        user2 = CustomUser(username='najef', email='new_najef@gmail.com')
        with self.assertRaises(IntegrityError):
            user2.save()
    
    def test_avoid_duplicate_email(self):

        user1 = CustomUser(username='christine', email='christine@gmail.com')
        user1.save()

        user2 = CustomUser(username='christine', email='christine@gmail.com')
        with self.assertRaises(IntegrityError):
            user2.save()