# -*- coding: utf-8 -*-
"""
A thin wrapper around gcloud.bucket with convenience
methods to interact with buckets

    >>> from gstorage.bucket import Bucket
    >>> bucket = Bucket()
    >>> bucket.sync_dir('/share/images')
"""

from gcloud.storage.bucket import Bucket as BaseBucket
from gcloud.storage.client import Client

from .utils import get_config


class Bucket(BaseBucket):

    def __init__(self, bucket=None, project=None):
        credentials = get_config('GOOGLE_APPLICATION_CREDENTIALS')
        if not project:
            project = get_config('GCLOUD_PROJECT_NAME')
        client = Client(credentials=credentials, project=project)
        return super(Bucket, self).__init__(client, bucket)
