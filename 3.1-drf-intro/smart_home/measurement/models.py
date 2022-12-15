from django.db import models

 
class Sensor(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100, null=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)
