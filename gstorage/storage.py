# -*- coding: utf-8 -*-
"""
gstorage.storage
~~~~~~~~~~~~~~~~

Implement the interface expected by :class:`django.core.files.storage.Storage`

    >>> from django.core.files.uploadfile import TemporaryUploadedFile
    >>> from gstorage.storage import Storage
    >>> storage = Storage(location='media/2016')
    >>> with TemporaryUploadedFile('test', 'text/plain', 1, 'utf8') as content:
    ...     storage.save('test.txt', content)
    ...
    >>> u'media/2016/test'
"""
import os

from django.core.files.storage import Storage as BaseStorage
from django.utils.crypto import get_random_string
from gcloud.storage.blob import Blob

from .bucket import Bucket


class Storage(BaseStorage):

    def __init__(self, location=None, base_url=None, bucket=None):
        self._location = location
        self._base_url = base_url
        if not bucket:
            self._bucket = Bucket.get_default()
        super(Storage, self).__init__()

    def _open(self, name, mode):
        """
        Retrieves the specified file from storage.
        """
        return Blob(name, self._bucket)

    def _save(self, name, content):
        """
        Saves new content to the file specified by name. The content should be
        a proper File object or any python file-like object, ready to be read
        from the beginning.
        """
        path = os.path.join(self._location, content.name) if self._location else content.name
        blob = Blob(path, self._bucket)
        blob.upload_from_file(content, size=content.size)
        return blob.name

    def get_valid_name(self, name):
        """
        Returns a filename, based on the provided filename, that's suitable for
        use in the target storage system.
        """
        return name

    def get_available_name(self, name):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """
        dir_name, file_name = os.path.split(name)
        file_root, file_ext = os.path.splitext(file_name)
        # If the filename already exists, add an underscore and a random 7
        # character alphanumeric string (before the file extension, if one
        # exists) to the filename until the generated filename doesn't exist.
        while self.exists(name):
            # file_ext includes the dot.
            name = os.path.join(dir_name, "%s_%s%s" % (file_root, get_random_string(7), file_ext))
        return name

    def path(self, name):
        """
        Returns a local filesystem path where the file can be retrieved using
        Python's built-in open() function. Storage systems that can't be
        accessed using open() should *not* implement this method.
        """
        raise NotImplementedError("This backend doesn't support absolute paths.")

    def delete(self, name):
        """
        Deletes the specified file from the storage system.
        """
        raise NotImplementedError('subclasses of Storage must provide a delete() method')

    def exists(self, name):
        """
        Returns True if a file referenced by the given name already exists in the
        storage system, or False if the name is available for a new file.
        """
        return Blob(name, self._bucket).exists()

    def listdir(self, path):
        """
        Lists the contents of the specified path, returning a 2-tuple of lists;
        the first item being directories, the second item being files.
        """
        raise NotImplementedError('subclasses of Storage must provide a listdir() method')

    def size(self, name):
        """
        Returns the total size, in bytes, of the file specified by name.
        """
        raise NotImplementedError('subclasses of Storage must provide a size() method')

    def url(self, name):
        """
        Returns an absolute URL where the file's contents can be accessed
        directly by a Web browser.
        """
        return Blob(name, self._bucket).public_url

    def accessed_time(self, name):
        """
        Returns the last accessed time (as datetime object) of the file
        specified by name.
        """
        raise NotImplementedError('subclasses of Storage must provide an accessed_time() method')

    def created_time(self, name):
        """
        Returns the creation time (as datetime object) of the file
        specified by name.
        """
        raise NotImplementedError('subclasses of Storage must provide a created_time() method')

    def modified_time(self, name):
        """
        Returns the last modified time (as datetime object) of the file
        specified by name.
        """
        raise NotImplementedError('subclasses of Storage must provide a modified_time() method')
