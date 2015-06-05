"""
Handling signals of the `core` app
"""

from django.dispatch import receiver

from core import signals
from critic import actions


@receiver(signals.app_link_ready)
def app_link_ready(sender, **kwargs):
    actions.create_app_links()
