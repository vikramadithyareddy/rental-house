from urllib import request

from django.db import models
from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
from django.contrib.auth.models import User
from hostupload.models import *

COLOR_CHOICES = (
    ('1','ONE'),
    ('2', 'TW0'),
    ('3','THREE'),

)
class detail(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()
    guests = models.IntegerField()
    singlerooms = models.CharField(max_length=6, choices=COLOR_CHOICES, default='1')
    singlerooms_attached = models.CharField(max_length=6, choices=COLOR_CHOICES, default='1')
    doublerooms = models.CharField(max_length=6, choices=COLOR_CHOICES, default='1')
    doublerooms_attached = models.CharField(max_length=6, choices=COLOR_CHOICES, default='1')
    triplerooms = models.CharField(max_length=6, choices=COLOR_CHOICES, default='1')
    triplerooms_attached = models.CharField(max_length=6, choices=COLOR_CHOICES, default='1')




