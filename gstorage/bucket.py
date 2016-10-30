# -*- coding: utf-8 -*-
"""
gstorage.bucket
~~~~~~~~~~~~~~~
A thin wrapper around gcloud.bucket with convenience
methods to interact with buckets

    >>> from gstorage.bucket import Bucket
    >>> bucket = Bucket.get_default()
    >>> bucket.copydir('/share/images')
"""
import os

from gcloud.storage.blob import Blob
from gcloud.storage.bucket import Bucket as BaseBucket
from gcloud.storage.client import Client
from oauth2client.client import GoogleCredentials

from .utils import find_files, get_config


class Bucket(BaseBucket):

    @classmethod
    def get_or_create(cls, bucket_name, client=None):
        """
        If the bucket exists with this name, get it. Else, create it

        :param cls: :class:`gstorage.bucket.Bucket`
        :type bucket_name: string
        :param bucket_name: name of the bucket
        :type client: gcloud.client.Client
        :param client: (optional) instance of client to use
        :return: :class:`Bucket <Bucket>` object
        :raises gcloud.exceptions.BadRequest (400): not a valid bucket name
        :raises gcloud.exceptions.Forbidden (403): The credentials are invalid
        """
        if not client:
            credentials = GoogleCredentials.get_application_default()
            client = Client(credentials=credentials)
        bucket = cls(client, name=bucket_name)
        if not bucket.exists():
            bucket.create()
        return bucket

    def copydir(self, path):
        """
        Copy the contents of the local directory given by path to google cloud.
        Maintain the same directory structure on remote.
        This is (intentionally) a blocking call, so clients can report errors if
        the transfer fails.

        :type path: string
        :param path: relative or absolute path to the directory that needs to be copied
        :return: True when transfer is complete
        :raises OSError: path doesn't exist or permission denied
        :raises ValueError: if the library cannot determine the file size
        :raises gcloud.exceptions.GCloudError: if upload status gives error response
        """
        if not os.access(path, os.R_OK):
            raise OSError('Permission denied')
        for filename in find_files(path):
            blob = Blob(filename, self)
            blob.upload_from_filename(filename)
        return True

    @classmethod
    def get_default(cls):
        """
        Get an instance of the default bucket identified fy GCLOUD_DEFAULT_BUCKET_NAME

        :param cls: :class:`gstorage.bucket.Bucket`
        :return: :class:`Bucket <Bucket>` object
        :raises gcloud.exceptions.BadRequest (400): not a valid bucket name
        :raises gcloud.exceptions.Forbidden (403): The credentials are invalid
        """
        return cls.get_or_create(get_config('GCLOUD_DEFAULT_BUCKET_NAME'))
