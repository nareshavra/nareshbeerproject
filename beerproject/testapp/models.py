from django.db import models
from django.urls import reverse

# Create your models here.
class BeerModel(models.Model):
    name=models.CharField(max_length=32)
    coo=models.CharField(max_length=32)
    price=models.FloatField()
    taste=models.CharField(max_length=32)
    poa=models.FloatField()

    def get_absolute_url(self):
        return reverse('beer')
