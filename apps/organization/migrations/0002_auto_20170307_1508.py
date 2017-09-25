# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-07 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('jg', '\u6559\u80b2\u673a\u6784'), ('gx', '\u9ad8\u6821'), ('gr', '\u4e2a\u4eba')], default='jg', max_length=20, verbose_name='\u673a\u6784\u7c7b\u522b'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to='org/%Y/%m', verbose_name='logo'),
        ),
    ]
