# Generated by Django 3.2.15 on 2023-10-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_migrate_dynamic_fields_to_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dynamic_fields',
            field=models.JSONField(editable=False, null=True),
        ),
    ]