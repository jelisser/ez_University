# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-02 01:10
from __future__ import unicode_literals

from django.db import migrations

from courseinfo.models import Semester

SEMESTERS = [
    {
        "semester_name": "2019 - Spring",
    },
    {
        "semester_name": "2019 - Summer",
    },
    {
        "semester_name": "2019 - Fall",
    },
    {
        "semester_name": "2020 - Spring",
    },
    {
        "semester_name": "2020 - Summer",
    },
    {
        "semester_name": "2020 - Fall",
    },
]


def add_semester_data(apps,schema_editor):
    Semseter = apps.get_model('courseinfo', 'Semester')
    for semester in SEMESTERS:
        semester_object = Semester.objects.create(
            semester_name=semester['semester_name'],
        )


def remove_semester_data(apps,schema_editor):
    Semester = apps.get_model('courseinfo', 'Semester')
    for semester in SEMESTERS:
        semester_object = Semester.objects.get(
            semester_name=semester['semester_name'],
        )
        semester_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0002_auto_20180401_2046'),
    ]

    operations = [
        migrations.RunPython(
            add_semester_data,
            remove_semester_data
        )
    ]
