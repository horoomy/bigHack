# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_application_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='rating',
            field=models.IntegerField(blank=True, default=0, verbose_name='рейтинг'),
        ),
    ]
