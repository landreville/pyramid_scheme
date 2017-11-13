from formencode import FancyValidator, Invalid
from pyramid_scheme.models import User


class UniqueUsername(FancyValidator):
    """Validate the username hasn't been taken."""

    def _validate_python(self, value, request):
        exists = (
            request.db.query(User)
            .filter(User.username == value)
            .count()
        )

        if exists:
            raise Invalid(
                'Username "{}" is already in use.'.format(value),
                value,
                request
            )
