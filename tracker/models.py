from django.db import models
from django.utils import timezone

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}, Timestamp: {self.timestamp}"

    # def __str__(self):
    #     return self.latitude
    
class FencedField(models.Model):
    point1lon = models.FloatField()
    point1lat = models.FloatField()
    
    point2lon = models.FloatField()
    point2lat = models.FloatField()
    
    point3lon = models.FloatField()
    point3lat = models.FloatField()
    
    point4lon = models.FloatField()
    point4lat = models.FloatField()
    
    
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"point1: {self.point1lon}, point2: {self.point2lon}, Timestamp: {self.timestamp}"
    
    