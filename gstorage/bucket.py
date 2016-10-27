# -*- coding: utf-8 -*-
"""
A thin wrapper around gcloud.bucket with convenience
methods to interact with buckets

    >>> from gstorage.bucket import Bucket
    >>> bucket = Bucket.get_or_create('pcaulagi')
    >>> bucket.sync_dir('/share/images')
"""

from gcloud.storage.bucket import Bucket as BaseBucket
from gcloud.storage.client import Client
from oauth2client.client import GoogleCredentials


class Bucket(BaseBucket):

    @classmethod
    def get_or_create(cls, bucket_name, client=None):
        """
        If the bucket exists with this name, get it. Else, create it

        Args:
            bucket_name: (string) name of the bucket
        Returns:
            an instance of bucket
        Raises:
            400: Bad request (the name is not valid)
            403: Forbidden (You don't have permissions for creating bucket)
        """
        if not client:
            credentials = GoogleCredentials.get_application_default()
            client = Client(credentials=credentials)
        bucket = cls(client, name=bucket_name)
        if not bucket.exists():
            bucket.create()
        return bucket
