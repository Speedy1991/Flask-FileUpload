"""
Flask-FileUpload
--------------
Flask-FileUpload is a Flask extension for easy file upload and management.
"""

from setuptools import setup, find_packages
import os
import re
import ast

BASE_PATH = os.path.dirname(__file__)


def get_requirements(suffix=''):
    with open(os.path.join(BASE_PATH, 'requirements%s.txt' % suffix)) as f:
        rv = f.read().splitlines()
    return rv

setup(
    name='Flask-FileUpload',
    version="0.5.0",
    url='https://github.com/speedy1991/Flask-FileUpload',
    license='MIT',
    author='Arthur Holzner',
    author_email='arthur.holz.91@gmail.com',
    description='Flask-FileUpload is a Flask extension for easy file upload and management',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=get_requirements(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
