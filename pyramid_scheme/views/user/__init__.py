"""
Package for managing users.

Include in the application setup::

    from pyramid_scheme.views import user

    def main():
        ...
        config.include(user)
        ...

"""
import logging
from .context import UsersContext, UserContext

log = logging.getLogger(__name__)


def includeme(config):
    # Route for actions that are for the set of users
    config.add_route(
        'users',
        '/users/{action}',
        factory=UsersContext
    )
    # Route for actions that are for a specific user
    config.add_route(
        'user',
        '/users/{action}/{username}',
        factory=UserContext
    )
