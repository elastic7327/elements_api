# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-28 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csv',
            name='type',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
