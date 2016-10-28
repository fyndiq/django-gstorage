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
    packagke_data={'': ['LICENSE', 'HISTORY.rst']},
    include_package_data=True,
    install_requires=[
        'Django',
        'gcloud',
    ],
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
