# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0007_auto_20160411_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='votingitem',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
