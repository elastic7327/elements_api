# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-28 15:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import engine.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('image', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'managed': True,
                'db_table': 'contents',
            },
        ),
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('archived_at', models.DateTimeField(auto_now=True, null=True)),
                ('file', models.FileField(null=True, upload_to=engine.models.upload_path_handler)),
                ('modified_at', models.DateField(auto_now=True, null=True)),
                ('archived', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
                'db_table': 'csvs',
            },
        ),
    ]
