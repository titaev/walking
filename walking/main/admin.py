from django.contrib import admin
from .models import City, Walk, WalkImage, Review
# Register your models here.

admin.site.register(City)
admin.site.register(Walk)
admin.site.register(WalkImage)
admin.site.register(Review)

