# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-05 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256),
        ),
    ]
