from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import City, Walk, Review
from .services import get_average_rating
from .forms import ReviewForm
from django.Http import HttpResponseRedirect


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
    review_form = ReviewForm()
    return render(request, 'main/walk.html',
                  {'walk': {'info': walk,
                            'rating': get_average_rating(walk.id)
                            },
                   'review_form': review_form
                   })

def rating(request, walk_id):
    if request.method == "POST":
        data = ReviewForm(request.POST)
        if data.is_valid():
            Review.object.create(user=request.user.id,
                                 walk=walk_id,
                                 rating=data.cleaned_data['rating'],
                                 description=data.cleaned_data['description'])
            return HttpResponseRedirect('/')

def about(request):
    return render(request, 'main/about.html')
