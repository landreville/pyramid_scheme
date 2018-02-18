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


def save(request, on_success_path, user=None, password=None):

    try:
        form_result = AddUserSchema().to_python(
            request.params,
            request
        )
    except Invalid as e:
        log.debug('Validation error: {}'.format(e))
        return {'form_errors': e.unpack_errors()}

    if not user:
        user = User()

    user.username = form_result['username']
    user.first_name = form_result['first_name']
    user.last_name = form_result['last_name']
    user.email = form_result['email']
    if password:
        user.password = password

    request.db.add(user)
    log.info('Saved new user {}'.format(user.username))
    return HTTPFound(on_success_path)


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

        return save(
            self._request,
            self._request.route_path('users'),
            password=self._random_password()
        )

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
    @view_config(
        renderer='templates/user-edit.mako',
        match_param='action=edit',
        request_method='GET'
    )
    def view(self):
        user = self._context.user
        return {
            'user': user,
            'edit_link': self._request.route_path(
                'user',
                action='edit',
                username=user.username
            )
        }

    @view_config(
        renderer='templates/user-edit.mako',
        request_method="POST",
    )
    def edit_save(self):
        user = self._context.user
        return save(
            self._request,
            self._request.route_path(
                'user',
                action='view',
                username=user.username
            ),
            user=user
        )
