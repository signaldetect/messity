"""
Application configuration of the `reader` app
"""

from django.apps import AppConfig
from django.conf import settings


class ReaderConfig(AppConfig):
    name = 'reader'
    verbose_name = 'Reader'

    def ready(self):
        # Definers of signals
        from reader import signals
        # Handlers of signals from other apps
        if 'storage' in settings.INSTALLED_APPS:
            from reader.receivers import storage
        if 'navigation' in settings.INSTALLED_APPS:
            from reader.receivers import navigation
        if 'core' in settings.INSTALLED_APPS:
            from reader.receivers import core
