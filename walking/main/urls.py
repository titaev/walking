from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('walk/', views.walk, name='walk'),
    path('FAQ/', views.about_site, name='FAQ')


    # path('second/', views.second_page, name='second'),
    # path('second/another/', views.another_page, name='another')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
