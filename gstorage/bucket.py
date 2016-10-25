# -*- coding: utf-8 -*-
"""
A thin wrapper around gcloud.bucket with convenience
methods to interact with buckets

    >>> from gstorage.bucket import Bucket
    >>> bucket = Bucket()
    >>> bucket.sync_dir('/share/images')
"""

from gcloud.bucket import Bucket as BaseBucket


class Bucket(BaseBucket):

    def __init__(self, name=None):
        pass

    def sync_dir(self, path):
        pass
