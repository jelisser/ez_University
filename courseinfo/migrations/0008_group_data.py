from __future__ import unicode_literals

from django.db import migrations


GROUPS = [
    {
        "name": "CourseInfoUser",
    },
    {
        "name": "CourseInfoScheduler",
    },
    {
        "name": "CourseInfoRegistrar",
    },
]


def add_group_data(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_object = Group.objects.create(
            name=group['name'],
        )


def remove_group_data(apps, schema_editor):
    Group = apps.get_model('auth','Group')
    for group in GROUPS:
        group_object=Group.objects.get(
            name=group['name']
        )
        group_object.delete()


class Migration(migrations.Migration):
    dependencies =[
        ('courseinfo', '0007_instructor_data'),
    ]

    operations =[
        migrations.RunPython(
            add_group_data,
            remove_group_data
        )
    ]
