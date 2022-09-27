from django.db import models

# Create your models here.

class Publications(models.Model):
    name = models.CharField(max_length=50)
