# -*- coding: utf-8 -*-
"""
gstorage.utils
~~~~~~~~~~~~~~

Helper functions used by other modules
"""
import os

from django.conf import settings


def get_config(key):
    """
    Get the value of config from settings. Else get it from environment.

    :type key: string
    :param key: A string indicating the key to config, for ex - GOOGLE_APPLICATION_CREDENTIALS

    :returns: The value of the key if present, else None
    """
    try:
        return getattr(settings, key)
    except AttributeError:
        try:
            return os.environ[key]
        except KeyError:
            pass
    return None


def find_files(path):
    """
    Return only the files under the given path

    :type key: string
    :param path: relative or absolute path to the directory
    :return: List of string where each item is a filepath
    """
    return [os.path.join(dirpath, file)
            for (dirpath, dirs, files) in os.walk(path)
            for file in files]
