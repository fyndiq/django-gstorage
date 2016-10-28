# -*- coding: utf-8 -*-
"""
Tests for gstorage.bucket
"""
import tempfile
from mock import MagicMock, patch
from os import environ
from unittest import TestCase

from gcloud.exceptions import BadRequest

from gstorage.bucket import Bucket


class TestBucket(TestCase):

    @classmethod
    def setUpClass(cls):
        if 'GOOGLE_APPLICATION_CREDENTIALS' in environ:
            del environ['GOOGLE_APPLICATION_CREDENTIALS']
        if 'GCLOUD_PROJECT' in environ:
            del environ['GCLOUD_PROJECT']

    @patch('gstorage.bucket.GoogleCredentials')
    @patch('gstorage.bucket.Client')
    def test_call_to_client(self, mock_client, mock_credentials):
        Bucket.get_or_create('test')
        assert mock_client.called

    @patch('gstorage.bucket.Client')
    def test_no_call_to_client(self, mock_client):
        Bucket.get_or_create('test', client=mock_client)
        assert not mock_client.called

    @patch('gstorage.bucket.Bucket.create')
    def test_bucket_exists(self, mock_create):
        Bucket.exists = MagicMock(return_value=True)
        Bucket.get_or_create('test', client='test')
        assert not mock_create.called

    @patch('gstorage.bucket.Bucket.create')
    def test_bucket_doesnot_exist(self, mock_create):
        Bucket.exists = MagicMock(return_value=False)
        Bucket.get_or_create('test', client='test')
        assert mock_create.called

    def test_bucket_badrequest(self):
        Bucket.exists = MagicMock(return_value=False)
        with patch('gstorage.bucket.Bucket.create', MagicMock(side_effect=BadRequest('400'))):
            with self.assertRaises(BadRequest):
                bucket = Bucket.get_or_create('test', client='test')
                assert bucket is None

    @patch('gstorage.bucket.GoogleCredentials')
    @patch('gstorage.bucket.get_config')
    def test_get_default(self, mock_get_config, mock_credentials):
        environ['GCLOUD_PROJECT'] = 'test'
        Bucket.get_default()
        assert mock_get_config.called_once_with('GCLOUD_DEFAULT_BUCKET_NAME')

    def test_copydir_noaccess(self):
        bucket = Bucket('test')
        with self.assertRaises(OSError):
            bucket.copydir('/root')

    def test_copydir_with_children(self):
        path = tempfile.mkdtemp()
        _, filename = tempfile.mkstemp(dir=path)

        bucket = Bucket('test')
        with patch('gstorage.bucket.Blob') as mock_blob:
            bucket.copydir(path)
            assert mock_blob.call_count == 1
