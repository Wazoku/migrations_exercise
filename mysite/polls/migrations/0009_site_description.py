# Generated by Django 3.2.15 on 2023-09-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_added_name_to_site_bio_to_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
