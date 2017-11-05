import logging

log = logging.getLogger(__name__)


from sqlalchemy import engine_from_config
from sqlalchemy.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from zope.sqlalchemy import ZopeTransactionExtension


METADATA = MetaData(naming_convention={
    "ix": '%(table_name)s_%(column_0_name)s_idx',
    "uq": "%(table_name)s_%(column_0_name)s_uk",
    "ck": "%(table_name)s_%(constraint_name)s_ck",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey"
})


BASE = declarative_base(metadata=METADATA)


def get_db(request):
    """
    Retrieve the persistent database pool from the registry.

    If the database pool has not been created yet then it is created
    and stored on the registry. A single instance will be created for the
    application.

    :param request: Current request.
    :type request: :class:`pyramid.request.Request`
    :return: SQLAlchemy database session.
    :rtype: :class:`sqlalchemy.orm.session.Session`
    """
    registry = request.registry
    try:
        db = registry.db
    except AttributeError:
        db = None

    if not db:
        db = registry.db = setup_db(request.registry.settings)

    return db


def setup_db(settings, prefix='sqlalchemy.'):
    """
    Create an SQLAlchemy database pool.
    """
    engine = engine_from_config(settings, prefix=prefix)
    maker = sessionmaker(bind=engine, extension=ZopeTransactionExtension())
    session = scoped_session(maker)
    BASE.metadata.bind = session.bind
    return session



