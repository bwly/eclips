# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20170318_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barber',
            name='avgRating',
        ),
        migrations.RemoveField(
            model_name='client',
            name='avgRating',
        ),
        migrations.AddField(
            model_name='barber',
            name='skills',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='barber',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='barber',
            name='price',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='barber',
            name='walkin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
