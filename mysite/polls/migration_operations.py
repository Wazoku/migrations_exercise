"""
Custom migration operations for supporting making changes to databases without downtime.
"""
import textwrap

from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.operations.fields import RemoveField
from django.db.migrations.state import ProjectState


class HideField(RemoveField):
    """
    Remove a field from the Django model state, but only set the field as nullable
    in the database, doing nothing in reverse.

    This operation makes it easier to remove fields without downtime.
    """

    def describe(self):
        return "Hide field %s from %s" % (self.name, self.model_name)

    def database_forwards(
        self,
        app_label: str,
        schema_editor: BaseDatabaseSchemaEditor,
        from_state: ProjectState,
        to_state: ProjectState,
    ) -> None:
        from_model = from_state.apps.get_model(app_label, self.model_name)

        if self.allow_migrate_model(schema_editor.connection.alias, from_model):
            from_field = from_model._meta.get_field(self.name)
            m2m_db_table = None

            if hasattr(from_field, 'm2m_db_table'):
                m2m_db_table = from_field.m2m_db_table()

            # Make the field nullable if needed.
            if not from_field.null and not m2m_db_table:
                to_field = from_field.clone()
                to_field.column = from_field.column
                to_field.null = True

                with schema_editor.connection.cursor() as cursor:
                    # Only make columns nullable when they exist
                    # We need to skip columns that don't exist
                    cursor.execute(
                        textwrap.dedent("""
                            SELECT EXISTS (
                                SELECT
                                FROM information_schema.columns
                                WHERE table_schema=%s
                                AND table_name=%s
                                AND column_name=%s
                            )
                        """),
                        (
                            schema_editor.connection.schema_name,
                            from_model._meta.db_table,
                            from_field.name,
                        )
                    )
                    column_exists = cursor.fetchone()[0]

                if column_exists:
                    schema_editor.alter_field(from_model, from_field, to_field)

    def database_backwards(
        self,
        app_label: str,
        schema_editor: BaseDatabaseSchemaEditor,
        from_state: ProjectState,
        to_state: ProjectState,
    ) -> None:
        # Do nothing when migrating the database backwards.
        # Fields set to NULL have to be kept as nullable, as new NULL values
        # will break removing NULL from the field.
        pass


class RemoveHiddenField(RemoveField):
    """
    Remove a field from the database without modifying model state, such as a
    field that has been previously hidden.

    The field will not be recovered after it is removed.
    """

    def __init__(self, model_name: str, name: str):
        super().__init__(model_name, name)
        self.elidable = True

    def state_forwards(self, app_label: str, state: ProjectState) -> None:
        pass

    def database_forwards(
        self,
        app_label: str,
        schema_editor: BaseDatabaseSchemaEditor,
        from_state: ProjectState,
        to_state: ProjectState,
    ) -> None:
        from_model = from_state.apps.get_model(app_label, self.model_name)
        if self.allow_migrate_model(schema_editor.connection.alias, from_model):
            sql = schema_editor.sql_delete_column % {
                "table": schema_editor.quote_name(from_model._meta.db_table),
                "column": schema_editor.quote_name(self.name),
            }
            schema_editor.execute(sql)

    def database_backwards(
        self,
        app_label: str,
        schema_editor: BaseDatabaseSchemaEditor,
        from_state: ProjectState,
        to_state: ProjectState,
    ) -> None:
        pass
