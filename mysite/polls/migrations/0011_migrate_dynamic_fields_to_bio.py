# Generated by Django 3.2.15 on 2023-10-04 15:05
import json
from django.db import migrations

def forwards_func(apps, schema_editor):
    Profile = apps.get_model("polls", "Profile")

    for obj in Profile.objects.all():
        try:
            obj.bio = json.dumps(obj.dynamic_fields)
            obj.save()
        except json.decoder.JSONDecodeError as e:
            print('Cannot convert {} object'.format(obj.pk))


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_profileform_is_active'),
    ]

    operations = [
        migrations.RunPython(
            forwards_func,
            migrations.RunPython.noop,
            elidable=True,
        ),
    ]
