# -*- coding: utf-8 -*-
"""
Check that the module is registered with required settings
"""

from os import environ

from django.conf import settings
from django.core import checks

from .constants import REQUIRED_SETTINGS


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


def check_gstorage_params(**kwargs):
    """
    Check that the module is initialized with all the required settings/environment

    Args:
        kwargs: optional list of app_config

    Returns:
        A list of errors
    """
    errors = []
    module_name = 'gstorage'

    for index, field in enumerate(REQUIRED_SETTINGS):
        if not get_config(field):
            errors.append(
                checks.Error(
                    '%s is required' % field,
                    hint=None,
                    obj=module_name,
                    id='%s.00%s' % (module_name, index + 1)  # use 1-based index for errors
                )
            )
    return errors
