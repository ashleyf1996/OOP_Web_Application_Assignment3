from django import forms
from .models import Event


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_location', 'event_type', 'upload_photo']

