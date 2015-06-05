"""
Handling signals of the `core` app
"""

from django.dispatch import receiver
from django.core.urlresolvers import reverse_lazy

from core import signals
from navigation import urls
from navigation import actions


@receiver(signals.app_link_ready)
def app_link_ready(sender, base_pattern, url_name, text, **kwargs):
    urls.app_urls['core'] = base_pattern
    urls.nav_links['core'] = {'url': reverse_lazy(url_name), 'text': text}


@receiver(signals.launched)
def launched(sender, **kwargs):
    actions.create_routers()
    actions.create_nav()
