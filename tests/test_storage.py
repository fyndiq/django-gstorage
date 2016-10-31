# -*- coding: utf-8 -*-
"""
Tests for gstorage.storage
"""
from mock import MagicMock, patch
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

    @patch('gstorage.storage.Blob')
    def test_exists(self, mock_blob, mock_bucket):
        mock_blob.exists = MagicMock()
        s = Storage()
        s.url('test.jpg')
        mock_blob.exists.call_count == 1

    @patch('gstorage.storage.Blob')
    def test_url(self, mock_blob, mock_bucket):
        mock_blob.public_url = MagicMock()
        s = Storage()
        s.url('test.jpg')
        mock_blob.public_url.call_count == 1

    @patch('gstorage.storage.Blob.exists')
    def test_available_name(self, mock_exists, mock_bucket):
        mock_exists.return_value = False
        s = Storage()
        assert s.get_available_name('test.jpg') == 'test.jpg'

    def test_valid_name(self, mock_bucket):
        s = Storage()
        assert s.get_valid_name('test.jpg') == 'test.jpg'

    def test_not_implemented(self, mock_bucket):
        s = Storage()
        with self.assertRaises(NotImplementedError):
            s.listdir('test')
        with self.assertRaises(NotImplementedError):
            s.path('test')
        with self.assertRaises(NotImplementedError):
            s.delete('test')
        with self.assertRaises(NotImplementedError):
            s.size('test')
        with self.assertRaises(NotImplementedError):
            s.accessed_time('test')
        with self.assertRaises(NotImplementedError):
            s.created_time('test')
        with self.assertRaises(NotImplementedError):
            s.modified_time('test')
