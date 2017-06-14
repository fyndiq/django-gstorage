django-gstorage
===============

.. image:: https://img.shields.io/pypi/v/django-gstorage.svg
   :alt: PyPi page
   :target: https://pypi.python.org/pypi/django-gstorage

.. image:: https://travis-ci.org/fyndiq/django-gstorage.svg?branch=master
    :alt: Travis CI Status
    :target: https://travis-ci.org/fyndiq/django-gstorage

.. image:: https://coveralls.io/repos/github/fyndiq/django-gstorage/badge.svg?branch=master
   :alt: Coverage status
   :target: https://coveralls.io/github/fyndiq/django-gstorage?branch=master

.. image:: https://readthedocs.org/projects/django-gstorage/badge/?version=latest&style=flat
   :alt: ReadTheDocs
   :target: https://django-gstorage.readthedocs.io/en/latest/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :alt: License MIT
   :target: https://github.com/fyndiq/django-gstorage/blob/master/LICENSE

.. image:: https://img.shields.io/gitter/room/nwjs/nw.js.svg
   :alt: Chat on gitter
   :target: https://gitter.im/django-gstorage/Lobby


This library is intended to be a 'plug-and-play' replacement
for `django.core.files.storage.FileSystemStorage` but reading
and writing files from Google storage. So there are two goals -

- It should be possible to use this library in projects already
  using local filesystem but which want to start using Google storage.
  In this case, we read from Google storage but if that fails, read
  from local filesystem and also update Google storage.

- Make it simpler to use newer features of Google storage like
  encrypting files with sensitive information

  .. code-block:: python

	order_pdf = FileField(encrypted=True)

Examples
++++++++

Using the module to upload some files

.. code-block:: python

    >>> from gstorage.bucket import Bucket

    >>> bucket = Bucket.get_default()
    >>> bucket.copydir('share/storage/2016/10/01')

Running Tests
+++++++++++++

    >>> pip install -r tests/requirements.txt
    >>> make test
