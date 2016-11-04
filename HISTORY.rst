.. :changelog:

Release history
---------------

0.5.1 (2016-11-04)
++++++++++++++++++++++

- ``gstorage.storage.Storage`` implements the interface expected from
  ``django.core.files.storage.Storage``.  The only **supported interface**
  at this point is ``storage._save``, and other methods are experimental.
- Support Python 3.4 for new Django (1.9 and 1.10)
- Added an example project showing use of django-gstorage

0.4.1 (2016-10-30)
++++++++++++++++++

- Updated docstrings to sphinx style
- Added documentation for gstorage.utils

0.4.0 (2016-10-30)
++++++++++++++++++

**Features**

- Refactored tests and added seperate test files for each module.
- Updated documentation on readthedocs.io to include section about
  bucket.

0.3.0 (2016-10-28)
++++++++++++++++++

**Features**

- ``gstorage.bucket.Bucket.get_default`` allowing easy access to
  default bucket.
- ``gstorage.bucket.Bucket.copydir`` allowing easy upload of files
  to Google cloud.
