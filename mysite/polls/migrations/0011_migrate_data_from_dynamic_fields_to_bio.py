from django import apps
from django.db import migrations
from django.db.models import F


def copy_field(apps, schema):
    model = apps.get_model('polls', 'profile')
    model.objects.all().update(bio=F('dynamic_fields'))


class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0010_profileform_is_active'),
    ]

    operations = [
        migrations.RunPython(
            code=copy_field,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
