from django.db import migrations
from polls.migration_operation import HideField


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_add_fields_data_field_to_profile_form_model'),
    ]

    operations = [
        HideField(
            model_name='ProfileForm',
            name='form_fields',
        ),
    ]
