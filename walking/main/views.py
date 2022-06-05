from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from .models import City, Walk


def index(request):
    result = City.objects.all()
    # result = [element.name for element in result]
    # page = requests.get("https://xn----7sbiew6aadnema7p.xn--p1ai/alphabet.php", verify=False)
    # soup = BeautifulSoup(page.text, "html.parser")
    # result = soup.find("div", {"class": "common-text"}).find("ul").find_all("li")
    # result = [element.text for element in result]
    return render(request, "main/index.html", {'cities': result})


def walk(request):
    city_id = request.GET.get('city')
    walk = Walk.objects.get(city=city_id)
    print()
    return render(request, 'main/walk.html', {"walk": walk})


def about(request):
    return render(request, 'main/about.html')
