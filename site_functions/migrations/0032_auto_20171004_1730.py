# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-04 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_functions', '0031_auto_20170920_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='curso',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='instituicao',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='local_de_atuacao',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profissao',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
