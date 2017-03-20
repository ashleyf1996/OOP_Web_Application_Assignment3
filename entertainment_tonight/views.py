from django.http import Http404
from django.shortcuts import render
from .models import Cities
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    all_cities = Cities.objects.all()
    return render(request, 'index.html', {'all_cities': all_cities})


def detail(request, cities_id):
    try:
        city = Cities.objects.get(pk=cities_id)
    except Cities.DoesNotExist:
        raise Http404("Sorry error!!")
    return render(request, 'detail.html', {'city': city})


class CitiesCreate(CreateView):
    model = Cities
    fields = ['town_name']





