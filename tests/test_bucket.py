# -*- coding: utf-8 -*-
"""
Tests for gstorage.bucket
"""
from mock import patch, MagicMock
from os import environ
from unittest import TestCase

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
        bucket = Bucket.get_or_create('test')
        assert mock_client.called

    @patch('gstorage.bucket.Client')
    def test_no_call_to_client(self, mock_client):
        bucket = Bucket.get_or_create('test', client=mock_client)
        assert not mock_client.called

    @patch('gstorage.bucket.Bucket.create')
    def test_bucket_exists(self, mock_create):
        Bucket.exists = MagicMock(return_value=True)
        bucket = Bucket.get_or_create('test', client='test')
        assert not mock_create.called

    @patch('gstorage.bucket.Bucket.create')
    def test_bucket_doesnot_exist(self, mock_create):
        Bucket.exists = MagicMock(return_value=False)
        bucket = Bucket.get_or_create('test', client='test')
        assert mock_create.called
