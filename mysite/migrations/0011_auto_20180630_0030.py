# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_auto_20180630_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prono',
            name='check_in',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
