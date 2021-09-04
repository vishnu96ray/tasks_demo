from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    geolocation = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Route(models.Model):
    school_id = models.ForeignKey(School, related_name='school_name',  on_delete=models.CASCADE, null=True, blank=True)
    start_time_scheduled = models.DateTimeField(verbose_name='start time scheduled', auto_now_add=True)
    stops = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.school_id)
