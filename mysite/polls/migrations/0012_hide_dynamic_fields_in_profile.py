from django.db import migrations, models

class HideField(migrations.RemoveField):
    def __init__(self, model_name, name):
        super().__init__(model_name, name)

    def describe(self):
        return "Hide field %s.%s" % (self.model_name, self.name)

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        # dynamic_fields is already null, so we don't need to do anything
        pass

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        """ rename it back """
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_migrate_data_from_dynamic_fields_to_bio'),
    ]

    operations = [
        HideField(model_name='profile', name='dynamic_fields'),
    ]
