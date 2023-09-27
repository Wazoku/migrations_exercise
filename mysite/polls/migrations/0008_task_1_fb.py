# Generated by Django 3.2.5 on 2021-09-26 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_add_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='name',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='bio',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
