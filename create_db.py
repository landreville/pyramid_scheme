"""
Create database tables and insert a user.
"""
import os
import transaction
from pyramid_scheme.models.meta import setup_db, METADATA
from pyramid_scheme.models import User


def main():
    # The database URL could be fetched from the development.ini file
    # directly, but it's easy enough to copy it here.
    here = os.getcwd()
    db = setup_db({
        'sqlalchemy.url': 'sqlite:///{}/database.db'.format(here)
    })

    # SQLAlchemy will create all the tables we have imported.
    # pyramid_scheme.models imports all models in it's __init__.py
    # therefore by importing anything in pyramid_scheme.models we have
    # implicitly imported all model classes
    METADATA.create_all(db.bind)

    # Add an initial user to allow logging in right away.
    db.add(User(
        username='admin',
        password='mypass',
        first_name='Norville',
        last_name='Rogers',
        email='norville@example.com',
    ))

    # setup_db adds a transaction manager to the database session
    # (for Pyramid integration).
    # Which requires using the transaction library for committing changes.
    transaction.commit()
    db.close()


if __name__ == '__main__':
    main()
