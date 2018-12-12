from django.db import models

# Create your models here.
class variables(models.Model):
    selected = models.CharField(max_length=200)

from django.contrib.auth.models import User

