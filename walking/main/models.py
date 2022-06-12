from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class City(models.Model):
    # id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Walk(models.Model):
    name = models.CharField(max_length=300)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    distance = models.FloatField()
    description = models.TextField()
    map = models.FileField(upload_to='maps/')

    def __str__(self):
        return self.name


class WalkImage(models.Model):
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE)
    image = models.FileField(upload_to='walks/')


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField(blank=True)


