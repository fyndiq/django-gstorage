"""
    django-gstorage
    ~~~~~~~~~~~~~~~
"""
import re

from setuptools import setup

version = ''
with open('gstorage/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(), re.MULTILINE).group(1)

with open('README.rst', 'r') as f:
    readme = f.read()
with open('HISTORY.rst', 'r') as f:
    history = f.read()

setup(
    name='django-gstorage',
    version=version,
    description='Allow easy integration with Google storage for Django projects',
    long_description=readme + '\n\n' + history,
    author='Pradip Caulagi',
    author_email='caulagi@gmail.com',
    url='http://github.com/fyndiq/django-gstorage/',
    packages=['gstorage'],
    package_data={'': ['LICENSE', 'HISTORY.rst']},
    include_package_data=True,
    install_requires=[
        'Django',
        'gcloud',
    ],
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
