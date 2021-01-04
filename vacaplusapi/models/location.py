from vacaplusapi.models import activity
from vacaplusapi.models.vacauser import VacaUser
from django.db import models
from .vacauser import VacaUser


class Location(models.Model):

    time = models.DateField(models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True))
    user = models.ForeignKey(VacaUser, on_delete=models.DO_NOTHING, related_name="vacauser")
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    activity = models.TextField(max_length=200)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)