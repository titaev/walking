from django.shortcuts import render
from .models import City, Walk, Review
from .services import get_avg_rating
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def index(request):
    result = City.objects.all()
    return render(request, 'main/index.html', {'cities': result})


def walk(request):
    city_id = request.GET.get('city')
    walk = Walk.objects.get(city=city_id)
    review_form = ReviewForm()
    return render(request, 'main/walk.html',
                  {"walk": {
                            'info': walk,
                            'rating': get_avg_rating(walk.id)
                            },
                   'review_form': review_form
                   })


def rating(request, walk_id):
    if request.method == "POST":
        data = ReviewForm(request.POST)
        walk = Walk.objects.get(id=walk_id)
        city_id = walk.city_id

        if data.is_valid():
            Review.objects.create(user_id=request.user.id,
                                  walk_id=walk_id,
                                  rating=data.cleaned_data['rating'],
                                  description=data.cleaned_data['description']
                                  )
            return HttpResponseRedirect(f'/walk/?city={city_id}')

