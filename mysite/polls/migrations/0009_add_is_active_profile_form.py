from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
            ('polls', '0008_add_Description_field_site'),
        ]

    operations = [
        migrations.AddField(
            model_name='profileform',
            name='is_active',
            field=models.BooleanField(
                default=True,
                null=True
                )
        ),
    ]
