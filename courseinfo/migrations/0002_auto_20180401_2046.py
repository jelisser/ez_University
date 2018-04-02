# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-02 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['course_number']},
        ),
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['course__course_number', 'section_name', 'semester__semester_name']},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ['semester_name']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterField(
            model_name='student',
            name='nickname',
            field=models.CharField(blank=True, default='', max_length=45),
        ),
    ]
