import logging
from . import meta
from .auth import User, Group, Permission

log = logging.getLogger(__name__)


def includeme(config):
    config.add_request_method(meta.get_db, 'db', reify=True)
