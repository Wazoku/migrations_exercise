# Generated by Django 3.2.19 on 2023-09-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_answer_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]