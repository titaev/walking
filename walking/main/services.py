from django.db.models import Avg

from .models import Rewiew

def get_avg_rating(walk_id):
    rate = Rewiew.objects.filter(walk=walk_id, rating__isnull=False).aggregate(avr=Avg('rating'))['avr']
    return round(rate, 1)

