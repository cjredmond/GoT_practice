# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('motto', models.CharField(max_length=50, null=True)),
                ('sigil', models.FileField(upload_to='')),
                ('region', models.CharField(max_length=40)),
                ('major', models.BooleanField()),
            ],
        ),
    ]
