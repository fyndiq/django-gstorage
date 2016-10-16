# django-gstorage

[![build-status-badge]][travis-url]
[![coveralls-badge]][coveralls-url]

This library is intended to be a 'plug and play' replacement
for `django.core.files.storage.FileSystemStorage` but reading
and writing files from Google storage. So there are two goals -

* It should be possible to use this library in projects already
using local filesystem but which want to start using Google storage.
In this case, we read from Google storage but if that fails, read
from local filesystem and also update Google storage.

* Make it simpler to use newer features of Google storage like
encrypting files with sensitive information

```
order_pdf = FileField(encrypted=True)
```


[build-status-badge]: https://travis-ci.org/fyndiq/django-gstorage.svg?branch=master
[travis-url]: https://travis-ci.org/fyndiq/django-gstorage
[coveralls-badge]: https://coveralls.io/repos/github/fyndiq/django-gstorage/badge.svg?branch=master
[coveralls-url]: https://coveralls.io/github/fyndiq/django-gstorage?branch=master
