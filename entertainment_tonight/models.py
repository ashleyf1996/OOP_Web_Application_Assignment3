import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# here are all of my models


class Cities(models.Model):
    town_name = models.CharField(max_length=200)


    # this function filters out what it to be printed. Puts it into a string
    def __str__(self):
        return self.town_name


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_location = models.CharField(max_length=200)
    event_address = models.CharField(max_length=200)
    event_type = models.CharField(max_length=200)
    upload_photo = models.FileField()
    event_creator = models.ForeignKey(User)



    def __str__(self):
        return self.event_name


class Type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Types'



