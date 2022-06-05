from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=300)


class Walk(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    distance = models.FloatField()
    description = models.TextField()
    map = models.FileField(upload_to='media/maps/')


class WalkImage(models.Model):
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE)
    image = models.FileField(upload_to='media/walks/')


class Review(models.Model):
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
