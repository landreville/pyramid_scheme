import logging
from pyramid.view import view_config, view_defaults
from pyramid_scheme.views import BaseView

log = logging.getLogger(__name__)


@view_defaults(route_name='users')
class UsersView(BaseView):
    """View-class for managing the set of users."""

    @view_config(
        renderer='templates/users.mako',
        match_param="action=index"
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

    @view_config(
        renderer='templates/user-add.mako',
        match_param="action=add",
        request_method="GET",
    )
    def add(self):
        return {}

    @view_config(
        renderer='templates/user-add.mako',
        match_param="action=add",
        request_method="POST",
    )
    def add_save(self):
        return {}


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
