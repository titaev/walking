from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from .models import City,Walk


def index(request):
    # page = requests.get('https://города-россия.рф/alphabet.php', verify=False)
    # soup = BeautifulSoup(page.text, "html.parser")
    # result = soup.find('div', {'class': "common-text"}).find('ul').find_all('li')
    # result = [element.text for element in result]
    result = City.objects.all()
    # result = [element.name for element in result]
    return render(request, 'main/index.html', {'cities': result})


def walk(request):
    city_id = request.GET.get('city')
    walk = Walk.objects.get(city=city_id)

    return render(request, 'main/walk.html', {'walk': walk})

def information(request):

    return render(request, 'main/information.html', {})


# def second_page(request):
#
#     return HttpResponse("Hello, world. You're at the second index.")
#
#
# def third_page(request):
#     return HttpResponse("Hello, world. You're at the third index.")

