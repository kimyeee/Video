# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-18 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='cover',
            field=models.CharField(max_length=128, verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=64, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='video',
            name='summarize',
            field=models.CharField(max_length=1024, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='video',
            name='type',
            field=models.CharField(max_length=32, verbose_name='类型'),
        ),
    ]
