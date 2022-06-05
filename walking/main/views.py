from django.shortcuts import render
from .models import City


def index(request):
    # page = requests.get('https://xn----7sbiew6aadnema7p.xn--p1ai/alphabet.php')
    # soup = BeautifulSoup(page.text, 'html.parser')
    #
    # result = soup.find('div', {'class': "common-text"}).find('ul').find_all('li')
    # result = [element.text for element in result]
    result = City.objects.all()
    result = [element.name for element in result]
    return render(request, 'main/index.html', {'cities': result})


def walk(request):
    city = request.GET.get('city')
    return render(request, 'main/walk.html', {"city": city})

def about_site(request):
    return render(request, 'main/FAQ.html')


# def second_page(request):
#     return HttpResponse("Second Hello")
#
#
# def another_page(request):
#     return HttpResponse("Another Page")
