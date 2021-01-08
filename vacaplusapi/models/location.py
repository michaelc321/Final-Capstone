# from vacaplusapi.models import Activity
# from vacaplusapi.models.vacauser import VacaUser
from django.db import models
# 


class Location(models.Model):

    time = models.DateField(models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True))
    user = models.ForeignKey("VacaUser", on_delete=models.DO_NOTHING, related_name="vacauser")
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    activity = models.ForeignKey("Activity", on_delete=models.DO_NOTHING, related_name="activity")
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)