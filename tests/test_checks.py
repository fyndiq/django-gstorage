# -*- coding: utf-8 -*-
"""
Tests for checking the configuration for app has
the valid checks (gstorage.apps, gstorage.checks)
"""
from mock import patch
from os import environ
from unittest import TestCase

from django.conf import settings

from gstorage.checks import check_gstorage_params

key = 'GOOGLE_APPLICATION_CREDENTIALS'


@patch('gstorage.checks.REQUIRED_SETTINGS', [key])
class TestStorageConfig(TestCase):

    def setUp(self):
        try:
            del environ[key]
        except KeyError:
            pass

    def test_key_error(self):
        """Test that app check throws an error when required setting is missing"""
        errors = check_gstorage_params()
        assert len(errors) >= 1
        assert errors[0].id == 'gstorage.001'
        assert errors[0].msg.find(key) == 0

    def test_key_settings(self):
        """Test that app check has no errors when settings is specified"""
        setattr(settings, key, '/tmp')
        assert check_gstorage_params() == []

    def test_key_env(self):
        """Test that app check has no errors when settings is specified as environment variable"""
        environ[key] = '/tmp'
        assert check_gstorage_params() == []
