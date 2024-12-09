import contextvars
from django.db import connections
from .utils import tenant_db_from_request

# Define a context variable for the database
db_context = contextvars.ContextVar("db_context")

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the tenant database from the request (based on domain/subdomain)
        db = tenant_db_from_request(request)
        # Set the database context for the request lifecycle
        db_context.set(db)
        response = self.get_response(request)
        return response

def get_current_db_name():
    """
    Utility method to retrieve the current database context
    """
    return db_context.get(None)

def set_db_for_router(db):
    """
    Utility method to set the database context for router
    """
    db_context.set(db)
