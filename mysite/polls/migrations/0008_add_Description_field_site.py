from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_answer_poll'),
                ]

    operations = [
        migrations.AddField(
            model_name="site",
            name="description",
            field=models.TextField(
                max_length=500,
                null=True
                ),
        ),
    ]
