from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings
# Create your models here.
class Doctor(AbstractUser):
    docSpec = models.CharField(max_length=225)
    spec = models.CharField(max_length=225)