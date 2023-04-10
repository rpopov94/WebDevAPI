# Getting Started

This is a basic template for a Django project using the Django Rest Framework (DRF), Djoser, and Poetry as a dependency manager.

Requirements
* Python 3.9 or higher
* Poetry

## Installation

Clone the repository

`git clone https://github.com/rpopov94/WebDevAPI.git`

Navigate into the project directory

`cd WebDevAPI`

Install dependencies using Poetry

`poetry install`

`poetry shell`

Run migrations

`python manage.py migrate`

Create a superuser account

`python manage.py createsuperuser`

Run the development server

`python manage.py runserver`

You can now access the DRF API at http://127.0.0.1:8000/api/ and the Djoser authentication endpoints at http://127.0.0.1:8000/auth/.

Usage
This template provides a basic setup for a Django + DRF + Djoser project. You can customize it as per your project requirements.

