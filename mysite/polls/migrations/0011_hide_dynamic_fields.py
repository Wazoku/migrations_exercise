from django.db import migrations

from polls.utils import HideField


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_profile_migrate_dynamic_fields_to_bio'),
    ]

    operations = [
        HideField(
            model_name='profile',
            name='dynamic_fields',
        ),
    ]
