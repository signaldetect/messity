"""
Application configuration of the `critic` app
"""

from django.apps import AppConfig
from django.conf import settings


class CriticConfig(AppConfig):
    name = 'critic'
    verbose_name = 'Critic'

    def ready(self):
        # Definers of signals
        from critic import signals
        # Handlers of signals from other apps
        if 'storage' in settings.INSTALLED_APPS:
            from critic.receivers import storage
        if 'navigation' in settings.INSTALLED_APPS:
            from critic.receivers import navigation
        if 'core' in settings.INSTALLED_APPS:
            from critic.receivers import core
