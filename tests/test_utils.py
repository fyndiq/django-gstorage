# -*- coding: utf-8 -*-
"""
Tests for gstorage.utils
"""
import os
import tempfile
from mock import patch
from unittest import TestCase

from django.conf import settings

from gstorage.apps import GStorageConfig
from gstorage.utils import find_files, get_config

key = 'GOOGLE_APPLICATION_CREDENTIALS'


class TestUtil(TestCase):

    def setUp(self):
        try:
            del os.environ[key]
        except KeyError:
            pass

    def test_find_files_empty_directory(self):
        path = tempfile.mkdtemp()
        assert find_files(path) == []

    def test_find_files_one_file(self):
        path = tempfile.mkdtemp()
        _, filename = tempfile.mkstemp(dir=path)
        assert find_files(path) == [filename]

    def test_find_files_with_children(self):
        path = tempfile.mkdtemp()
        _, filename = tempfile.mkstemp(dir=path)
        child = tempfile.mkdtemp(dir=path)
        _, child_filename = tempfile.mkstemp(dir=child)

        assert find_files(path) == [filename, child_filename]

    @patch('gstorage.checks.REQUIRED_SETTINGS', [key])
    def test_key_override(self):
        """Test that config retains the value in settings over environment"""
        setattr(settings, key, '/foo')
        os.environ[key] = '/bar'
        assert get_config(key) == '/foo'

    @patch('gstorage.checks.REQUIRED_SETTINGS', [key])
    def test_real_config(self):
        """Test that instantiating the real config calls the validation methods"""
        with patch('gstorage.apps.checks.register') as mock_method:
            app = GStorageConfig.create('gstorage')
            app.ready()
            assert mock_method.call_count == 1
