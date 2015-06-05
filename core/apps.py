"""
Application configuration of the `core` app
"""

from django.apps import AppConfig
from django.conf import settings


class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = 'Core'

    def ready(self):
        # Definers of signals
        from core import signals
        # Handlers of signals from other apps
        if 'navigation' in settings.INSTALLED_APPS:
            from core.receivers import navigation
        # Launches the `core` app
        from core import actions
        actions.launch()
