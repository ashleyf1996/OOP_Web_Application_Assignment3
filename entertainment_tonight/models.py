from django.db import models


# here are all of my models

class Cities(models.Model):
    town_name = models.CharField(max_length=200)
    town_picture = models.CharField(max_length=400)


