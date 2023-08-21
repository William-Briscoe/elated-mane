"""Hair styles class module"""
from django.db import models
from django.contrib.auth.models import User

class HairStyle(models.Model):
    """Hair style model class"""
    label = models.CharField(max_length=50)