from formencode import Schema
from formencode.validators import UnicodeString, Email
from .validators import UniqueUsername


class AddUserSchema(Schema):

    username = UniqueUsername(not_empty=True)
    first_name = UnicodeString(not_empty=True)
    last_name = UnicodeString(not_empty=True)
    email = Email(not_empty=True)


