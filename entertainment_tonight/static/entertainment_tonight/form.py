from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.models import Event

class EventCreate(CreateView):
    # trying to create a new event
    model = Event
    fields = ['event_name', 'event_location', 'event_type']
