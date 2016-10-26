# -*- coding: utf-8 -*-
"""
A thin wrapper around gcloud.bucket with convenience
methods to interact with buckets

    >>> from gstorage.bucket import Bucket
    >>> bucket = Bucket()
    >>> bucket.sync_dir('/share/images')
"""

from gcloud.bucket import Bucket as BaseBucket
from gcloud.client import Client

from .utils import get_config


class Bucket(BaseBucket):

    def __init__(self, bucket_name=None, project_name=None):
        credentials = get_config('GOOGLE_APPLICATION_CREDENTIALS')
        if not project_name:
            project_name = get_config('GCLOUD_PROJECT_NAME')
        client = Client(credentials, project=project_name)
        return super(BaseBucket, self).__init__(self, client, name=bucket_name)

    def sync_dir(self, path):
        pass
