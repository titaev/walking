from django.db.models import Avg
from.models import Review


def get_average_rating(walk_id):
    rate = Review.objects.filter(walk=walk_id, rating__isnull=False).aggregate(avr=Avg('rating'))['avr']
    return round(rate, 1)
