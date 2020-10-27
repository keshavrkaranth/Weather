from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=20,null=True)
    temprature = models.FloatField(max_length=6,null=True)
    description = models.TextField(null=True)
    icon = models.CharField(max_length=5,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

