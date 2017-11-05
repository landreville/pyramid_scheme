import logging
from pyramid.httpexceptions import HTTPNotFound

from pyramid_scheme.views.context import BaseContext
from pyramid_scheme.models import User


log = logging.getLogger(__name__)


class UsersContext(BaseContext):

    def get_users(self):
        """Return query for all Users."""
        return self._db.query(User).order_by(User.username)


class UserContext(BaseContext):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
