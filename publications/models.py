from email.policy import default
from django.db import models

# Create your models here.

class Publications(models.Model):
    name = models.CharField(max_length=50)
    las_name = models.CharField(max_length=50, default="")
    email = models.EmailField(default="email@mail.ru")
    patronim = models.CharField(max_length=50, default="Василич")


class Template(models.Model):
    name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    publication = models.ForeignKey(to=Publications, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(max_length=10)
    publication = models.ForeignKey(to=Publications, on_delete=models.CASCADE)
    template = models.ForeignKey(to=Template, on_delete=models.CASCADE)



