# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-23 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0012_auto_20160423_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='votingitem',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]