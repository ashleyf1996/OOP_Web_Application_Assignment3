# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment_tonight', '0021_event_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
