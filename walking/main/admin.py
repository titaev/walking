from django.contrib import admin
from .models import City, Walk, WalkImage,Rewiew
admin.site.register(City)
# Register your models here.
admin.site.register(Walk)
admin.site.register(WalkImage)
admin.site.register(Rewiew)