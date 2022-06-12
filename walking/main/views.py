from django.shortcuts import render
# from .services import get_all_cities
from .models import City, Walk, Review
from .services import get_avg_rating
from .forms import ReviewForm
from django.http import HttpResponseRedirect
def index(request):
    # result = get_all_cities()
    result = City.objects.all()
    # result = [element.name for element in result]

    return render(request, 'main/index.html', {'cities': result})


def walk(request):
    city_id = request.GET.get('city')
    walk = Walk.objects.get(city=city_id)
    review_form = ReviewForm()
    # здесь делаем запрос в базу
    return render(request, 'main/walk.html',
                  {"walk": {'info': walk,
                            "rating": get_avg_rating(walk.id)
                            },
                   'review_form': review_form
                   })


def rating(request, walk_id):
    print(walk_id)
    if request.method == "POST":
        data = UserRegistrationForm(request.POST)
        if data.is_valid():
            Review.objects.create(user=request.user.id,
                                  walk=walk_id,
                                  rating=data.cleaned_data['rating'],
                                  description=data.cleaned_data['description']
                                  )
            return HttpResponseRedirect('/')