"""
Handling signals of the `navigation` app
"""

from django.dispatch import receiver

from navigation import signals
from reader import views


@receiver(signals.nav_ready)
def nav_ready(sender, template, context, **kwargs):
    views.HallView.template_base = template
    views.HallView.extra_context = context.get('reader', {})
