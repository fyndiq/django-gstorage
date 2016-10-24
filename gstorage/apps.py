# -*- coding: utf-8 -*-
"""
Specify the config for the module used to install the app
"""
from django.apps import AppConfig
from django.core import checks
from django.utils.translation import ugettext_lazy as _

from .checks import check_gstorage_params


class GStorageTestConfig(AppConfig):
    """A test config which initializes the app without checks at startup"""
    name = 'gstorage'
    verbose_name = _('Django GStorage')


class GStorageConfig(GStorageTestConfig):

    def ready(self):
        checks.register(checks.Tags.models)(check_gstorage_params)
