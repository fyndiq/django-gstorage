# -*- coding: utf-8 -*-
"""
Check that the module is registered with required settings
"""
from django.core import checks

from .constants import REQUIRED_SETTINGS
from .utils import get_config


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
