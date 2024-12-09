def tenant_db_from_request(request):
    """
    Function to determine the tenant database based on the request's domain.
    This is a simplified version without database lookup.
    """
    # Extract the hostname from the request (e.g., "tenant1.example.com")
    host = request.get_host().split(':')[0]  # Ignore port if present
    subdomain = host.split('.')[0]
    # Check the host and return the corresponding tenant database
    print(subdomain)
    if subdomain == 'tenant1':
        return 'tenant1'  # Use tenant1 database
    elif subdomain == 'tenant2':
        return 'tenant2'  # Use tenant2 database
    else:
        return 'default'  # Fallback to default database if no match
