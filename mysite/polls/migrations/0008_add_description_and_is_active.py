# Generated by Django 3.2.15 on 2023-10-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_answer_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
