from django.db import models

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
# Create your models here.

class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)

class Walk(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    distance = models.FloatField()
    description = models.TextField()
    map = models.FileField(upload_to='media/maps/')


class Rewiew(models.Model):
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)], blank=True)
    description = models.TextField(blank=True)


class WalkImage(models.Model):
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE)
    image = models.FileField(upload_to='media/walks/')
