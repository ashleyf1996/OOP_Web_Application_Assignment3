# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment_tonight', '0003_event_upload_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='upload_photo',
            field=models.FileField(upload_to=b''),
        ),
    ]
