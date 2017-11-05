import logging
import crypt
from sqlalchemy import (
    Column, ForeignKey, Table, Unicode, Integer
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from .meta import BASE

log = logging.getLogger(__name__)


class User(BASE):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(Unicode, nullable=False, unique=True)
    first_name = Column(Unicode)
    last_name = Column(Unicode)
    email = Column(Unicode, nullable=False)
    _password = Column('password', Unicode, nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        # Store the password as a salted hash
        self._password = crypt.crypt(password, crypt.mksalt())

    def verify_password(self, input_password):
        """Check that the given password is corret for this user."""
        return self._password == crypt.crypt(input_password, self._password)


users_groups_table = Table(
    'users_groups',
    BASE.metadata,
    Column(
        'user_id',
        ForeignKey(User.user_id, ondelete="CASCADE"),
        primary_key=True,
        nullable=False
    ),
    Column(
        'group_id',
        Integer,
        ForeignKey('groups.group_id', ondelete="CASCADE"),
           primary_key=True,
        nullable=False
    ),
)


class Group(BASE):
    __tablename__ = 'groups'

    group_id = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False)
    description = Column(Unicode)

    users = relationship(
        User,
        secondary=users_groups_table,
        backref='groups'
    )


groups_permissions = Table(
    'groups_permissions',
    BASE.metadata,
    Column(
        'group_id',
        ForeignKey(Group.group_id, ondelete="CASCADE"),
        primary_key=True,
        nullable=False
    ),
    Column(
        'permission_id',
        Integer,
        ForeignKey('permissions.permission_id', ondelete="CASCADE"),
        primary_key=True,
        nullable=False
    ),
)


class Permission(BASE):
    __tablename__ = 'permissions'

    permission_id = Column(Unicode, primary_key=True)
    description = Column(Unicode)

    groups = relationship(
        Group,
        secondary=groups_permissions,
        backref='permissions'
    )
