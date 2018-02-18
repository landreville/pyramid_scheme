from formencode import FancyValidator, Invalid
from pyramid_scheme.models import User


class UniqueUsername(FancyValidator):
    """Validate the username hasn't been taken."""

    def _validate_python(self, value, request):
        try:
            current_user = request.context.user
        except AttributeError:
            # Must be on the add page
            pass
        exists = (
            request.db.query(User)
            .filter(User.username == value)
        )
        if current_user:
            exists = exists.filter(User.username != current_user.username)

        if exists.count():
            raise Invalid(
                'Username "{}" is already in use.'.format(value),
                value,
                request
            )
