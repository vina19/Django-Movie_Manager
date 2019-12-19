from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError
from movie_superfan.models import Movie, Comment, UserProfile, CustomUser

# Test the string for displaying the movie
class TestMovieModel(TestCase):

    def test_str_movie_title(self):

        movie_name = Movie(name='Parasit')
        self.assertEqual(str(movie_name), movie_name.name)

# Test the string for displaying the comment
class TestCommentModel(TestCase):

    def test_str_comment_title(self):

        movie = Movie(name='Parasit')
        user1 = CustomUser(username='najef')
        comment_title = Comment(user=user1, movie_title=movie)
        self.assertEqual(str(comment_title), 'Comment from user ID {} for movie {}'.format(comment_title.user, comment_title.movie_title))

# Test the string for displaying the user profile
class TestUserProfileModel(TestCase):

    def test_str_userprofile_title(self):
        
        user1 = CustomUser(username='najef')
        user_profile = UserProfile(user=user1)
        self.assertEqual(str(user_profile), '{} Profile'.format(user_profile.user))

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