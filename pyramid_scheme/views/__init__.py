"""
Contains view-packages.

Each view-package is a python sub-package containing the view-callables,
templates, contexts, etc necessary for displaying and managing a single
entity.

Entity is loosely defined; best practices for separation of concerns
should be used to decide whether to make a new view-package. Most view-packages
should be easily extractable to it's own Pyramid application.
"""
import logging
from .base import BaseView

log = logging.getLogger(__name__)


