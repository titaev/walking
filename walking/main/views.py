from django.shortcuts import render
from .models import City, Walk


def index(request):
    result = City.objects.all()
    return render(request, 'main/index.html', {'cities': result})


def walk(request):
    city_id = request.GET.get('city')
    walk = Walk.objects.get(city=city_id)
    print(walk.map)
    return render(request, 'main/walk.html', {"walk": walk})



