# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-21 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='pre_learning',
            field=models.CharField(default='', max_length=300, verbose_name='\u8bfe\u7a0b\u987b\u77e5'),
        ),
    ]
