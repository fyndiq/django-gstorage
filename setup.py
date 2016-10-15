"""
django-gstorage

"""
import re
from setuptools import setup

version = ''
with open('gstorage/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(), re.MULTILINE).group(1)

setup(
    name='django-gstorage',
    version=version,
    description='Allow easy integration with Google storage for Django projects',
    long_description=__doc__,
    author='Pradip Caulagi',
    author_email='caulagi@gmail.com',
    url='http://github.com/fyndiq/django-gstorage/',
    packages=['gstorage'],
    include_package_data=False,
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
