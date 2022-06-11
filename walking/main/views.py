from django.shortcuts import render
# from .services import get_all_cities
from .models import City, Walk

def index(request):
    # result = get_all_cities()
    result = City.objects.all()
    # result = [element.name for element in result]

    return render(request, 'main/index.html', {'cities': result})


def walk(request):
    city_id = request.GET.get('city')
    walk = Walk.objects.get(city=city_id)
    # здесь делаем запрос в базу
    return render(request, 'main/walk.html', {"walk": walk})




