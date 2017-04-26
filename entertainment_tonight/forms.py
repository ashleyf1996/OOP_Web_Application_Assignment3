from django import forms
from .models import Event
from django.contrib.auth.models import User

# This is the form used to create the event


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'upload_photo', 'event_address','created_at','event_date']

    event_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    upload_photo = forms.FileField()
    event_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    created_at = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    event_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    # Meta class stores information about my class
    class Meta:
        model = User
        fields= ['username', 'email', 'password']