# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]