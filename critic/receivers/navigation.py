"""
Handling signals of the `navigation` app
"""

from django.dispatch import receiver

from navigation import signals
from critic import views


@receiver(signals.nav_ready)
def nav_ready(sender, template, context, **kwargs):
    views.ReviewView.template_base = template
    views.ReviewView.extra_context = context.get('critic_review', {})

    views.ThanksView.template_base = template
    views.ThanksView.extra_context = context.get('critic_send', {})
