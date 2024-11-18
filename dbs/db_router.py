class AppDatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'postgres':
            return 'default'
        elif model._meta.app_label == 'mongo':
            return 'mongo'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'postgres':
            return 'default'
        elif model._meta.app_label == 'mongo':
            return 'mongo'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Permite aplicar migraciones en la base de datos correcta para cada aplicación.
        """
        if app_label == 'postgres':
            return db == 'default'
        elif app_label == 'mongo':
            return db == 'mongo'
        return None