# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment_tonight', '0004_auto_20170410_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='upload_photo',
            field=models.FileField(blank=True, null=True, upload_to=b'media'),
        ),
    ]
