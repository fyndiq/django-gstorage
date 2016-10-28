# -*- coding: utf-8 -*-
"""
Tests for gstorage.utils
"""
import tempfile
from unittest import TestCase

from gstorage.utils import find_files


class TestUtil(TestCase):

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
