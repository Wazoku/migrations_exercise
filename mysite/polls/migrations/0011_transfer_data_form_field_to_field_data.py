# Add a second migration file to copy values from one field to another.
# The operations must be in a separate file, because UPDATE queries cannot
# be run in the same query as ALTER TABLE queries.
from django.db import migrations, models

from ..db.migration_operation import HideField


# For copying old values to the new field.
def copy_field_values(apps, schema_editor):
    ProfileForm = apps.get_model('polls', 'ProfileForm')

    profile_forms = ProfileForm.objects.all()

    for profile_form in profile_forms: 
        profile_form.fields_data = profile_form.form_fields

    ProfileForm.objects.bulk_update(profile_forms, ['fields_data'])


class Migration(migrations.Migration):
    
    dependencies = [
        ('polls', '0010_profileform_fields_data'),
    ]

    operations = [
        migrations.RunPython(
            copy_field_values,
            migrations.RunPython.noop,
            # The operation should be elidable, so it doesn't appear in the
            # squashed migration file.
            elidable=True,
        ),
    ]