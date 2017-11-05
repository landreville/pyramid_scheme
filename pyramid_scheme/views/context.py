

class BaseContext(object):
    """
    Base class for contexts.

    Most views in this app will use a database connection. This class will
    add an instance attribute for the database session and the request.
    """

    def __init__(self, request):
        self._request = request
        self._db = self._request.db
