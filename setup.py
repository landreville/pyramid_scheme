from setuptools import find_packages, setup

entry_points = {
    'paste.app_factory': ['main = pyramid_scheme:main'],
}

install_requires = [
    'pyramid',
    'pyramid-exclog',
    'pyramid-mailer',
    'pyramid-mako',
    'pyramid-tm',
    'waitress',
    'sqlalchemy',
    'zope.sqlalchemy',
    'formencode',
]

development = ['pyramid-debugtoolbar']

# Install extras with:
# pip install -e "/path/to/pyramid_scheme[development]"
extras_require = {
    'development': development,
}

setup(
    name='pyramid_scheme',
    version='0.0.1',
    description='',
    author='',
    author_email='',
    packages=find_packages(),
    include_package_data=True,
    entry_points=entry_points,
    install_requires=install_requires,
    extras_require=extras_require
)
