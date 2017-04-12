from django.contrib import admin
from .models import Cities, Event, Type

# my models here.


admin.site.register(Cities)
admin.site.register(Event)
admin.site.register(Type)