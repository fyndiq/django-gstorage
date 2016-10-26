# -*- coding: utf-8 -*-
"""
Helper functions used by other modules
"""
from os import environ

from django.conf import settings


def get_config(key):
    """
    Get the value of config from settings. Else get it from environment.

    Args:
        key: A string indicating the key to config, for ex - GOOGLE_APPLICATION_CREDENTIALS

    Returns:
        The value of the key if present, else None
    """
    try:
        return getattr(settings, key)
    except AttributeError:
        try:
            return environ[key]
        except KeyError:
            pass
    return None
