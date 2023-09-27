from django.db import migrations

BATCH_SIZE = 100


def migrate_dynamic_fields_to_bio(apps, _):
    from polls.models import Profile

    profiles = Profile.objects.all()

    for profile in profiles:
        profile.bio = profile.dynamic_fields

    Profile.objects.bulk_update(profiles, ['bio'], batch_size=BATCH_SIZE)


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_profile_bio'),
    ]

    operations = [
        migrations.RunPython(
            migrate_dynamic_fields_to_bio,
            migrations.RunPython.noop,
            elidable=True,
        ),
    ]
