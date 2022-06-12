from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('walk/', views.walk, name='walk'),
    path('about', views.about, name='about'),
    path('walk/rating/<int:walk_id>', views.rating, name='rating')
]
