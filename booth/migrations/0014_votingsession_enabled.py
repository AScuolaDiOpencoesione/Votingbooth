# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0013_votingitem_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='votingsession',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
    ]