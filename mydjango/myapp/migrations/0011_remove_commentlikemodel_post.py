# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 06:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_commentlikemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentlikemodel',
            name='post',
        ),
    ]
