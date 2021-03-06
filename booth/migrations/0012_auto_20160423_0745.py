# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-23 07:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0011_auto_20160419_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voterelements',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, related_name='voters', to='booth.VotingElement'),
        ),
        migrations.AlterField(
            model_name='voterelements',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
