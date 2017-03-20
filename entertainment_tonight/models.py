from django.db import models


# here are all of my models


class Cities(models.Model):
    town_name = models.CharField(max_length=200)

    # this function filters out what it to be printed. Puts it into a string
    def __str__(self):
        return self.town_name




