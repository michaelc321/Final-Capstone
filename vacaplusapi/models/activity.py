from django.db import models
from .location import Location


class Activity(models.Model):

    title = models.CharField(max_length=50,)
    description = models.CharField(max_length=255,)
    date = models.DateField(default="0000-00-00",)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    locationId = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name="location")