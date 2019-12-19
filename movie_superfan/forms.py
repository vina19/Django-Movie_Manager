from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from .models import Movie, CustomUser

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise ValidationError('Please enter an email address')

        if CustomUser.objects.filter(email__iexact=email).exists():
            raise ValidationError('A user has already registered using this email')

        return email
    
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        
        return user

class WatchedMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'poster')
