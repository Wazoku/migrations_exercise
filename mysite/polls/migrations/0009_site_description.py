# Generated by Django 3.2.19 on 2023-09-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20230927_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]