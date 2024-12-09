class TenantRouter:
    """
    A router to control database operations for tenant-specific databases.
    """

    def db_for_read(self, model, **hints):
        tenant_db = hints.get('tenant_db')
        if tenant_db:
            return tenant_db
        return 'default'

    def db_for_write(self, model, **hints):
        tenant_db = hints.get('tenant_db')
        if tenant_db:
            return tenant_db
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_obj1 = hints.get('tenant_db', 'default')
        db_obj2 = hints.get('tenant_db', 'default')

        if db_obj1 == db_obj2:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that the tenant-specific models are migrated to the appropriate tenant database.
        """
        if db == 'default':
            # Run default app migrations in the default database
            return True
        elif db in ['tenant1', 'tenant2']:
            # Allow migrations for tenant databases
            return True
        return False
