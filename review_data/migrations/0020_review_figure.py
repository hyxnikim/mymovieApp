# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-29 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_data', '0019_auto_20181127_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='figure',
            field=models.ImageField(default=1, upload_to='figures/'),
            preserve_default=False,
        ),
    ]
