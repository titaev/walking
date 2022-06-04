from django.shortcuts import render
from .services import get_all_cities


def index(request):
    result = get_all_cities()
    return render(request, 'main/index.html', {'cities': result})


def walk(request):
    city = request.GET.get('city')
    # здесь делаем запрос в базу
    return render(request, 'main/walk.html', {"city": city})



