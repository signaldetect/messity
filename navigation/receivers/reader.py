"""
Handling signals of the `reader` app
"""

from django.dispatch import receiver
from django.core.urlresolvers import reverse_lazy

from reader import signals
from navigation import urls


@receiver(signals.app_link_ready)
def app_link_ready(sender, base_pattern, url_name, text, **kwargs):
    urls.app_urls['reader'] = base_pattern
    urls.nav_links['reader'] = {'url': reverse_lazy(url_name), 'text': text}
