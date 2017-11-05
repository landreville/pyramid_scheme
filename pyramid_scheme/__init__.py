
import logging
from pyramid.config import Configurator
from .views import user
from . import models

log = logging.getLogger(__name__)


def main(global_config, **app_settings):
    """
    Configure and instantiate the pyramid_scheme Pyramid application.
    """
    settings = global_config.copy()
    settings.update(app_settings)

    config = Configurator(
        settings=settings,
    )
    # Serve files in the static directory under /static URL
    config.add_static_view(
        name='static',
        path='pyramid_scheme:static'
    )
    config.include(models)
    config.include(user)
    config.scan()
    return config.make_wsgi_app()
