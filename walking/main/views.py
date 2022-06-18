from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from bs4 import BeautifulSoup
import requests
from .models import City, Walk, Rewiew
from .services import get_avg_rating
from .forms import RewiewForm



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
    rewiew_form = RewiewForm()

    return render(request, 'main/walk.html',
                  {'walk': {"info": walk, 'rating': get_avg_rating((walk.id))},
                   'rewiew_form': rewiew_form})


def rating(request, walk_id):
    if request.method =='POST':
        data = RewiewForm(request.POST)
        walk=Walk.objects.get(id=walk_id)
        city_id= walk.city_id
        if data.is_valid():
            user = User.objects.get(id=request.user.id)
            walk = Walk.objects.get(id=walk_id)

            Rewiew.objects.create(user=user,
                                  walk=walk,
                                  rating=data.cleaned_data['rating'],
                                  description=data.cleaned_data['description']
                                  )
            return HttpResponseRedirect(request.path_info)


def information(request):
    return render(request, 'main/information.html', {})

# def second_page(request):
#
#     return HttpResponse("Hello, world. You're at the second index.")
#
#
# def third_page(request):
#     return HttpResponse("Hello, world. You're at the third index.")
