"""
Application configuration of the `storage` app
"""

from django.apps import AppConfig
from django.conf import settings


class StorageConfig(AppConfig):
    name = 'storage'
    verbose_name = 'Storage'

    def ready(self):
        # Definers of signals
        from storage import signals
        # Handlers of own signals
        from storage import receivers
        # Handlers of signals from other apps
        if 'core' in settings.INSTALLED_APPS:
            from storage.receivers import core
