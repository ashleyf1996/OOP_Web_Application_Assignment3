from django import forms
from .models import Event
from django.contrib.auth.models import User


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'upload_photo', 'event_address','event_creator']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # information about your class

    class Meta:
        model = User
        fields= ['username', 'email', 'password']