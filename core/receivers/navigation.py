"""
Handling signals of the `navigation` app
"""

from django.dispatch import receiver

from navigation import signals
from core import views


@receiver(signals.nav_ready)
def nav_ready(sender, template, context, **kwargs):
    views.WelcomeView.template_base = template
    views.WelcomeView.extra_context = context.get('core', {})
