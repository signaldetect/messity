"""
Application configuration of the `navigation` app
"""

from django.apps import AppConfig
from django.conf import settings


class NavigationConfig(AppConfig):
    name = 'navigation'
    verbose_name = 'Navigation'

    def ready(self):
        # Definers of signals
        from navigation import signals
        # Handlers of signals from other apps
        if 'reader' in settings.INSTALLED_APPS:
            from navigation.receivers import reader
        if 'critic' in settings.INSTALLED_APPS:
            from navigation.receivers import critic
        if 'core' in settings.INSTALLED_APPS:
            from navigation.receivers import core
