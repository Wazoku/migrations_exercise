from django.db.models import F
from django.db import migrations


def copy_field_values(apps, schema_editor):
    ProfileForm = apps.get_model('polls', 'ProfileForm')

    ProfileForm.objects.update(fields_data=F('form_fields'))


def revert_field_values(apps, schema_editor):
    Community = apps.get_model('polls', 'ProfileForm')

    Community.objects.update(form_fields=F('fields_data'))


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20231004_1513'),
    ]

    operations = [
        migrations.RunPython(
            copy_field_values,
            revert_field_values,
            elidable=True,
        ),
    ]