# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment_tonight', '0014_event_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(verbose_name=b'%Y-%m-%d'),
        ),
    ]
