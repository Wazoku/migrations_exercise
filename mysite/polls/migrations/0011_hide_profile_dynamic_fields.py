# Generated by Django 3.2.15 on 2023-09-27 15:35

import polls.db.migration_operation
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_fill_bio_with_dynamic_fields'),
    ]

    operations = [
        polls.db.migration_operation.HideField(
            model_name='profile',
            name='dynamic_fields',
        ),
    ]
