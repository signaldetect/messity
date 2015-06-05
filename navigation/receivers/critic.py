"""
Handling signals of the `critic` app
"""

from django.dispatch import receiver
from django.core.urlresolvers import reverse_lazy

from critic import signals
from navigation import urls
from navigation import actions


@receiver(signals.app_link_ready)
def app_link_ready(sender, base_pattern, url_name, text, **kwargs):
    urls.app_urls['critic'] = base_pattern
    urls.nav_links['critic'] = {'url': reverse_lazy(url_name), 'text': text}


@receiver(signals.sub_link_ready)
def sub_link_ready(sender, url_name, text, alias, **kwargs):
    actions.extend_nav(app_name='critic', sub_name=alias)
    urls.nav_links[alias] = {'url': reverse_lazy(url_name), 'text': text}


@receiver(signals.sub_button_ready)
def sub_button_ready(sender, button_type, text, alias, **kwargs):
    actions.extend_nav(app_name='critic', sub_name=alias)
    urls.nav_links[alias] = {
        'url': '#', 'text': text, 'button_type': button_type
    }
