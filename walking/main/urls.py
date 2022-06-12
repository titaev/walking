
from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static



from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('walk/', views.walk, name='walk'),
    path('information/', views.information, name='info'),
    path('walk/rating/<int:walk_id>', views.rating, name='walk_rating'),
]
