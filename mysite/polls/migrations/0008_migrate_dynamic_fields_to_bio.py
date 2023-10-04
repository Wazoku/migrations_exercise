# Generated by Django 3.2.15 on 2023-09-27 15:27
import json
from django.db import migrations


def copy_dynamic_fields_to_biography(apps, schema_editor):
    Profile = apps.get_model('polls', 'Profile')
    for profile in Profile.objects.all():
        if profile.dynamic_fields:
            try:
                biography_value = profile.dynamic_fields.get('biography', '')
                profile.biography = json.dumps(biography_value)
                profile.save()
            except Exception as e:
                print(f'Error converting the object {profile.pk}: {e}')


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_answer_poll'),
    ]

    operations = [
        migrations.RunPython(copy_dynamic_fields_to_biography),
    ]