# -*- coding: utf-8 -*-
"""
Tests for gstorage.storage
"""
from mock import patch
from unittest import TestCase

from gstorage.storage import Storage


@patch('gstorage.storage.Bucket.get_default')
class TestStorage(TestCase):

    @patch('gstorage.storage.Blob')
    def test_save_no_location(self, mock_blob, mock_bucket):
        s = Storage()
        s._save('test.jpg', None)
        mock_blob.assert_called_once_with('test.jpg', mock_bucket())

    @patch('gstorage.storage.Blob')
    def test_save_with_location(self, mock_blob, mock_bucket):
        s = Storage(location='images')
        s._save('test.jpg', None)
        mock_blob.assert_called_once_with('images/test.jpg', mock_bucket())

    @patch('gstorage.storage.Blob')
    def test_open(self, mock_blob, mock_bucket):
        s = Storage()
        s._save('test.jpg', 'r')
        mock_blob.assert_called_once_with('test.jpg', mock_bucket())

    def test_get_valid_name(self, mock_bucket):
        s = Storage()
        assert s.get_valid_name('test.jpg') == 'test.jpg'
