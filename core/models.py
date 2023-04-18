from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core import managers

from ckeditor_uploader.fields import RichTextUploadingField

from typing import List
from django.core.files import File
from datetime import datetime


class CustomUser(AbstractUser):
    username: str | None = None
    email: str = models.EmailField(_('email address'), unique=True)
    bio: str = models.TextField()
    gender: str = models.CharField(
        max_length=140,
        null=True,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        )
    )
    birth_date: datetime = models.DateField(null=True, blank=True)
    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: List = []

    objects: object = managers.CustomUserManager()

    def __str__(self) -> str:
        return self.email


class Post(models.Model):
    title: str = models.CharField(max_length=200)
    content: str = RichTextUploadingField(config_name='default')
    image: File = models.ImageField(upload_to='images/')
    date_posted: datetime = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
