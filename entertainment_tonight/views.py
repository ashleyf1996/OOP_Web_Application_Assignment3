from django.http import HttpResponse
from django.template import loader
from .models import Cities


def index(request):
    template = loader.get_template('index.html')
    html = ''
    all_cities = Cities.objects.all()
    for city in all_cities:
        url = '/entertainment_tonight/' + str(city.id) + '/'
        html += '<a href="' + url +'">' + city.town_name + '</a> <br>'
    return HttpResponse(template.render(request), html)


def detail(request, cities_id):
    return HttpResponse("<h2>Details for city id: "+ str(cities_id) + "</h2>")


