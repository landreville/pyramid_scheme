"""
Database models.

This package also works as a Pyramid add-on to add a database session pool as
an attribute on the request. Include in the application configuration such as::

    from pyramid_scheme import models

    def main():
        ...
        config.include(models)
        ...

The database session will be available as "request.db". The configuration settings
must include "sqlalchemy.url" key. Note that the database will not be created
until it's first access on request.db.

This provides faster application startup, but may delay a failure until the first
request if the database cannot be created.

A future addition to this add-on could provide a configuration setting to instantiate
the database session on application startup.
"""
import logging
from . import meta
from .auth import User, Group, Permission

log = logging.getLogger(__name__)


def includeme(config):
    config.add_request_method(meta.get_db, 'db', reify=True)
