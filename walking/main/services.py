# from bs4 import BeautifulSoup
# import requests
from .models import Review
from django.db.models import Avg

# def get_all_cities():
#     page = requests.get('https://xn----7sbiew6aadnema7p.xn--p1ai/alphabet.php', verify=False)
#     soup = BeautifulSoup(page.text, "html.parser")
#     # print(page.text)
#
#     result = soup.find('div', {'class': "common-text"}).find("ul").find_all('li')
#     result = [element.text for element in result]
#     return result

def get_avg_rating(walk_id):
    rate = Review.objects.filter(walk=walk_id, rating__isnull=False).aggregate(avr=Avg('rating'))['avr']
    return round(rate, 1)
