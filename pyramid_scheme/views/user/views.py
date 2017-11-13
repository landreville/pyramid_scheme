import logging
import string
import random
from formencode import Invalid
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, view_defaults
from pyramid_scheme.views import BaseView
from pyramid_scheme.models import User
from .forms import AddUserSchema

log = logging.getLogger(__name__)


@view_defaults(route_name='users')
class UsersView(BaseView):
    """View-class for managing the set of users."""

    @view_config(
        renderer='templates/users.mako',
    )
    def view(self):
        users = self._context.get_users()

        # Generator of (user instance, link to view)
        users = ((user, self._make_view_link(user)) for user in users)

        return {
            'users': users
        }

    def _make_view_link(self, user):
        return self._request.route_path(
            'user',
            action='view',
            username=user.username
        )


@view_defaults(route_name='users add')
class UsersAddView(BaseView):

    @view_config(
        renderer='templates/user-add.mako',
        request_method="GET",
    )
    def add(self):
        return {}

    @view_config(
        renderer='templates/user-add.mako',
        request_method="POST",
    )
    def add_save(self):

        try:
            form_results = AddUserSchema().to_python(
                self._request.params,
                self._request
            )
        except Invalid as e:
            log.debug('Validation error: {}'.format(e))
            return {'form_errors': e.unpack_errors()}

        new_user = User(
            username=form_results['username'],
            first_name=form_results['first_name'],
            last_name=form_results['last_name'],
            email=form_results['email'],
            password=self._random_password()
        )

        self._request.db.add(new_user)
        log.info('Added new user {}'.format(new_user.username))
        return HTTPFound(self._request.route_path('users'))

    def _random_password(self):
        """Return a 12-character string with random letters and digits."""
        return ''.join([
            random.choice(string.ascii_letters + string.digits)
            for _ in range(12)
        ])


@view_defaults(route_name='user')
class UserView(BaseView):
    """View-class for managing a specific user."""

    @view_config(
        renderer='templates/user-view.mako',
        match_param="action=view"
    )
    def view(self):
        user = self._context.get_user()
        return {
            'user': user
        }
