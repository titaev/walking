from django.urls import path, include

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/delete', views.delete_acc, name='delete_acc'),
]
