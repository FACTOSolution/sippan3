# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_functions', '0020_minicurso_short_course_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minicurso',
            name='short_course_cover',
            field=models.ImageField(default=False, upload_to='minicursos/'),
        ),
    ]
