from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre

# Create your models here.
class User(AbstractUser):
    genre = models.IntegerField()
