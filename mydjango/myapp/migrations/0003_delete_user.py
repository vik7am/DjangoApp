# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 06:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_usermodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
