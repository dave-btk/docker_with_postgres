from os import name
from django.db import models

# Create your models here.

class Details(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)