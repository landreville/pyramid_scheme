import logging

log = logging.getLogger(__name__)


class BaseView(object):
    """
    Includes functionality that will be common to all view-classes
    in this application.

    Sets the current context and request as instance attributes _context
    and _request.
    """

    def __init__(self, context, request):
        self._context = context
        self._request = request
