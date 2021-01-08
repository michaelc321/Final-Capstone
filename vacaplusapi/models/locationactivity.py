from django.db import models
from .location import Location
from .activity import Activity



class LocationActivity(models.Model):

    location = models.ForeignKey("Location", on_delete=models.DO_NOTHING, related_name="location2")
    activity = models.ForeignKey("Activity", on_delete=models.DO_NOTHING, related_name="activity2")