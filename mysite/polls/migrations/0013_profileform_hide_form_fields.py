# Generated by Django 3.2.15 on 2023-10-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_profileform_form_fields_to_fields_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileform',
            name='form_fields',
            field=models.JSONField(blank=True, editable=False, null=True),
        ),
    ]
