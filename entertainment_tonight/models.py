from django.db import models
from django.core.urlresolvers import reverse

# here are all of my models


class Cities(models.Model):
    town_name = models.CharField(max_length=200)

    # this function filters out what it to be printed. Puts it into a string
    def __str__(self):
        return self.town_name


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_location = models.CharField(max_length=200)
    event_type = models.CharField(max_length=200)
    upload_photo = models.CharField(max_length=200)

    #when we create new event, it adds it to db and gives it id. go to detail view
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.event_name
