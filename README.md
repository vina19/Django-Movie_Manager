# Movie Manager
#### A web app that display the upcoming movie list from IMDB API which the user can see its movie detail information and the movie trailer from YOUTUBE API.
#### The user also able to register, login, logut, and mark watched and unwatched for the movie.

## Installation
    git clone https://github.com/vina19/django-movie-manager.git

## Getting Started
#### 1. Create and activate a virtual environment.
    Macs python3 -m venv env | env/bin/activate
    Windows PC python -m venv env | env/script/activate
#### 2. pip install -r requirements.txt
#### 3. python manage.py makemigrations movie_superfan
#### 4. python manage.py migrate
#### 5. python manage.py runserver
    Site at 127.0.0.1:8000
#### 6. From the command line load the API keys by run the source env.sh

## Run Test
    python manage.py test movie_superfan.tests.test_models
    python manage.py test movie_superfan.tests.test_views
    python manage.py test movie_superfan.tests.test_forms
    
## Live Link to Deployed App
[https://vina19.github.io/Django-Movie_Manager/](https://vina19.github.io/Django-Movie_Manager/)

## Login Page
![loginpage](https://user-images.githubusercontent.com/46719712/71199630-f8d07200-225b-11ea-88d8-a3f991c3f495.JPG)

## Register Form Page
![signuppage](https://user-images.githubusercontent.com/46719712/71199750-39c88680-225c-11ea-9717-a8c1299ebb99.JPG)

## Upcoming Movies Page
![movielist](https://user-images.githubusercontent.com/46719712/71199681-17cf0400-225c-11ea-9bd6-3e05658803e5.JPG)

## Movie Detail Page
![moviedetail](https://user-images.githubusercontent.com/46719712/71199686-1998c780-225c-11ea-8b02-619e7019df0e.JPG)

## User Profile Page
![userprofile](https://user-images.githubusercontent.com/46719712/71199696-1dc4e500-225c-11ea-8836-de958c6ce0a7.JPG)

## Logout Page
![logoutpage](https://user-images.githubusercontent.com/46719712/71199704-21586c00-225c-11ea-9c4e-b6acfbb5a0b8.JPG)

# API Used
#### IMDB API
#### YouTube API

# Created using:
#### - Django 19.0.3
#### - Python 3.7
#### - CSS
#### - Bootstrap

# Contact:
vinakurniasari94@gmail.com

## The MIT License (MIT)
#### Copyright © 2020 <Vina Kurniasari>

#### Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#### The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#### THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
