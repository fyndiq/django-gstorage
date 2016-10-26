# -*- coding: utf-8 -*-
"""
Tests for gstorage.bucket
"""
from mock import patch
from os import environ
from unittest import TestCase

from gstorage.bucket import Bucket


class TestBucket(TestCase):

    def setUp(self):
        try:
            del environ['GOOGLE_APPLICATION_CREDENTIALS']
        except KeyError:
            pass

    @patch('gstorage.bucket.Client')
    def test_default_constructor(self, mock_client):
        bucket = Bucket()
        assert bucket is not None
        mock_client.assert_called_once_with(credentials=None, project=None)

    @patch('gstorage.bucket.Client')
    def test_project(self, mock_client):
        Bucket(project='test')
        mock_client.assert_called_once_with(credentials=None, project='test')

    @patch('gstorage.bucket.Client')
    def test_credentials(self, mock_client):
        environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/tmp/test'
        Bucket()
        mock_client.assert_called_once_with(credentials='/tmp/test', project=None)
