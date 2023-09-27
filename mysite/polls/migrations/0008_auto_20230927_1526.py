# Generated by Django 3.2.15 on 2023-09-27 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_answer_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileform',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='site',
            name='description',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
