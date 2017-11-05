import os
import transaction
from pyramid_scheme.models.meta import setup_db, METADATA
from pyramid_scheme.models import User


def main():
    here = os.getcwd()
    db = setup_db({
        'sqlalchemy.url': 'sqlite:///{}/database.db'.format(here)
    })

    METADATA.create_all(db.bind)
    db.add(User(
        username='admin',
        password='mypass',
        first_name='Norville',
        last_name='Rogers',
        email='norville@example.com',
    ))
    transaction.commit()
    db.close()


if __name__ == '__main__':
    main()
