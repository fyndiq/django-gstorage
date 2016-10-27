# -*- coding: utf-8 -*-
"""
Tests for gstorage.bucket
"""
from mock import MagicMock, patch
from os import environ
from unittest import TestCase

from gcloud.exceptions import BadRequest

from gstorage.bucket import Bucket


class TestBucket(TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            del environ['GOOGLE_APPLICATION_CREDENTIALS']
        except KeyError:
            pass

    @patch('gstorage.bucket.Client')
    def test_call_to_client(self, mock_client):
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
