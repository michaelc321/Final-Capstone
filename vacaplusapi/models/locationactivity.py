from django.db import models




class LocationActivity(models.Model):

    location = models.ForeignKey("Location", on_delete=models.CASCADE, related_name="location2")
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE, related_name="activity2")
