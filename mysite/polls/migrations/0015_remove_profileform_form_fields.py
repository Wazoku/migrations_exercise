# Generated by Django 3.2.15 on 2023-09-27 15:38

from django.db import migrations
from polls.utils import HideField


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_profileform_fields_data'),
    ]

    operations = [
        HideField(
            model_name='profileform',
            name='form_fields',
        ),
    ]
