from .models import Review
from django.db.models import Avg


def get_avg_rating(walk_id):
    rate = Review.objects.filter(walk=walk_id, rating__isnull=False).aggregate(avr=Avg('rating'))['avr']
    return round(rate, 1)


