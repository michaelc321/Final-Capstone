from django.db import models
from .location import Location



class Activity(models.Model):

    name = models.CharField(max_length=50,)
