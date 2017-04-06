from django.contrib import admin
from .models import Cities, Event

# my models here.

admin.site.register(Cities)
admin.site.register(Event)