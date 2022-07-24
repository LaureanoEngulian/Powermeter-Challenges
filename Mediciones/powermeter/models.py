from django.db import models

# Create your models here.
class Medicion(models.Model):
    sensor_data = models.FloatField()