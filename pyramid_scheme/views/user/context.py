import logging
from pyramid.httpexceptions import HTTPNotFound

from pyramid_scheme.views.context import BaseContext
from pyramid_scheme.models import User


log = logging.getLogger(__name__)


class UsersContext(BaseContext):
    """Context class providing the set of users."""

    # Using a method called get_users instead of a property such as
    # "users" because a database query is a non-trivial amount of work.
    # The caller should be prompted to think about that and save the query results
    # rather than repeatedly calling context.users to get the results.
    def get_users(self):
        """Return query for all Users."""
        return self._db.query(User).order_by(User.username)


class UserContext(BaseContext):
    """Context class providing a specific user based on the URL."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Saving URL parameters on the context to allow them to be
        # used by multiple methods. This also isolates the place where
        # data is extracted from the request to a single place.
        # That will help to reduce duplication and possible typos when
        # writing the key names.
        self._username = self._request.matchdict['username']

    def get_user(self):
        """Return query for the user."""
        user = (
            self._db.query(User)
                .filter(User.username == self._username)
                .one_or_none()
        )
        if not User:
            # Convert to HTTPNotFound because the username in the URL is not found
            log.debug('Could not find user {}'.format(self._username))
            raise HTTPNotFound()
        return user
