# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-21 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_data', '0013_remove_review_movienum'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rmovie_num',
            field=models.IntegerField(default=0),
        ),
    ]
