from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('walk/', views.walk, name='walk'),
    path('FAQ/', views.about_site, name='FAQ')


    # path('second/', views.second_page, name='second'),
    # path('second/another/', views.another_page, name='another')
]
