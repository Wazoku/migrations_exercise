from django.db import migrations, models
from django.db.models import F


def migrate_from(apps, schema_editor):
    ProfileForm = apps.get_model('polls', 'ProfileForm')

    ProfileForm.objects.update(fields_data=F('form_fields'))


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_profileform_fields_data'),
    ]

    operations = [
        migrations.RunPython(
            code=migrate_from,
            reverse_code=migrations.RunPython.noop,
            elidable=True,
        )
    ]
