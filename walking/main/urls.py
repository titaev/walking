from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('walk/', views.walk, name='walk'),
    path('walk/rating/<int:walk_id>', views.rating, name='rating')
]

