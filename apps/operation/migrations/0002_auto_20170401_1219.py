# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-01 12:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAsk',
        ),
        migrations.DeleteModel(
            name='UserMessage',
        ),
    ]
