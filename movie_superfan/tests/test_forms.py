from django.test import TestCase

from django.contrib.auth.models import User
from movie_superfan.forms import UserRegisterForm, CustomUser
import string
    
class TestRegistrationFrom(TestCase):

    # Test if the register with the valid data
    def test_register_user_valid_data(self):
        user_data = { 'username' : 'najef', 'email' : 'najef@gmail.com', 'password1' : 'abcd1234defg', 'password2' : 'abcd1234defg' }
        form = UserRegisterForm(user_data)
        self.assertTrue(form.is_valid())
    
    # Test if the password1 and password2 unmatch
    def test_register_user_both_password_unmatch(self):
        user_data = { 'username' : 'najef', 'email' : 'najef@gmail.com', 'password1' : 'abcd1234defg', 'password2' : '1234abcd56defg' }
        form = UserRegisterForm(user_data)
        self.assertFalse(form.is_valid())
    
    # Test showing fails if the user trying to register with missing field data
    def test_register_user_missing_data_fails(self):
        user_data = { 'username' : 'najef', 'email' : 'najef@gmail.com', 'password1' : 'abcd1234defg', 'password2' : 'abcd1234defg' }

        for field in user_data.keys():
            data = dict(user_data)
            del(data[field])
            form = UserRegisterForm(data)
            self.assertFalse(form.is_valid())
    
    # Test if the username that register is already in database
    def test_register_username_already_exists_in_db(self):
        user1 = CustomUser(username='najef', email='najef@gmail.com')
        user1.save()

        user_data = { 'username' : 'najef', 'email' : 'new_najef@gmail.com', 'password1' : 'abcd1234defg', 'password2' : 'abcd1234defg' }
        form = UserRegisterForm(user_data)
        self.assertFalse(form.is_valid())
    
    # Test if the email that register is already in database
    def test_register_email_already_exists_in_db(self):
        user1 = CustomUser(username='najef', email='najef@gmail.com')
        user1.save()

        user_data = { 'username' : 'new_najef', 'email' : 'najef@gmail.com', 'password1' : 'abcd1234defg', 'password2' : 'abcd1234defg' }
        form = UserRegisterForm(user_data)
        self.assertFalse(form.is_valid())

class TestLoginForm(TestCase):

    # Test that the loging username and password match
    def test_username_password_valid(self):
        user1 = CustomUser(username='najef', email='najef@gmail.com')
        user1.save()

        user_data = { 'username' : 'najef', 'email' : 'new_najef@gmail.com', 'password1' : 'abcd1234defg', 'password2' : 'abcd1234defg' }
        form = UserRegisterForm(user_data)
        self.assertFalse(form.is_valid())