# Getting Started

This is a basic template for a Django project using the Django Rest Framework (DRF), Djoser, and Poetry as a dependency manager.

Requirements
* Python 3.7 or higher
* Poetry

## Installation

Clone the repository

`git clone https://github.com/your-username/project-name.git`

Navigate into the project directory

`cd project-name`

Create a new virtual environment

`python3 -m venv env`

Activate the virtual environment

On Linux and macOS:

`source env/bin/activate`

On Windows:

`env\Scripts\activate`

Install dependencies using Poetry

`poetry install`

Create a new Django project

`django-admin startproject config .`
Create a new Django app

`python manage.py startapp app_name`

Configure the Django project to use DRF and Djoser

Add the following to the `INSTALLED_APPS` section of config/settings.py:

```
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'djoser',
    # ...
]
```

Add the following to the urls.py file of the Django project:

```
from django.urls import include, path

urlpatterns = [
    # ...
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # ...
]
```

Run migrations

`python manage.py migrate`

Create a superuser account

`python manage.py createsuperuser`

Run the development server

`python manage.py runserver`

You can now access the DRF API at http://127.0.0.1:8000/api/ and the Djoser authentication endpoints at http://127.0.0.1:8000/auth/.

Usage
This template provides a basic setup for a Django + DRF + Djoser project. You can customize it as per your project requirements.

