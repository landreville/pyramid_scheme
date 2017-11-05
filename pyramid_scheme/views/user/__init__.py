import logging
from .context import UsersContext, UserContext

log = logging.getLogger(__name__)


def includeme(config):
    config.add_route(
        'users',
        '/users/{action}',
        factory=UsersContext
    )

    config.add_route(
        'user',
        '/users/{action}/{username}',
        factory=UserContext
    )
