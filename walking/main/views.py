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
        if data.is_valid():
            user = User.objects.get(id=request.user.id)
            walk = Walk.objects.get(id=walk_id)
            Review.objects.create(user=user,
                                  walk=walk,
                                  rating=data.cleaned_data['rating'],
                                  description=data.cleaned_data['description']
                                  )
            return HttpResponseRedirect('/')

