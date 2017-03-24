
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import CreateEventForm
from .models import Event


def index(request):
    all_events = Event.objects.all()
    return render(request, 'index.html', {'all_events': all_events})


class DetailView(generic.DeleteView):
    model = Event
    template_name = 'detail.html'


class EventCreate(CreateView):
    model = Event
    fields = ['event_name', 'event_type', 'event_location']


def home(request):
    form = CreateEventForm()
    context = {
        "form": form
    }
    return render(request, 'event_form.html', context)












