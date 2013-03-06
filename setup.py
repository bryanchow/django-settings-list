import os
from setuptools import setup, find_packages

version = '0.1'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-settings-list',
    version = version,
    description = "Django app that lists the settings values for a running " \
                  "project using a custom view accessible only by superusers.",
    long_description = read('README.rst'),
    classifiers = [],
    keywords = "",
    author = "Bryan Chow",
    author_email = '',
    url = 'https://github.com/bryanchow/django-settings-list',
    download_url = 'https://github.com/bryanchow/django-settings-list/tarball/master',
    license = "WTFPL",
    packages = find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'django',
    ],
)
