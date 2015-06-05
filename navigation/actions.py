"""
Actions of the `navigation` app
"""

from itertools import tee
from itertools import chain

from django.conf.urls import url
from django.conf.urls import include

from navigation import urls
from navigation import signals


def create_routers():
    """
    Sorts URLs by length of their patterns (short patterns moves to the bottom
    of the list) and then creates routers of URLs
    """
    app_urls = sorted(
        urls.app_urls.items(),
        key=lambda app_url: len(app_url[1]),  # app_urls: [(app_name, pattern)]
        reverse=True
    )
    urls.urlpatterns = [
        url(pattern, include(app_name + '.urls', namespace=app_name))
        for (app_name, pattern) in app_urls
    ]


def extend_nav(app_name, sub_name):
    """
    Extends the navigation by sub-navigation
    """
    idx = urls.nav_order.index(app_name)
    num_items = len(urls.nav_order)

    nav_item = urls.nav_order[idx + 1 - num_items]
    if isinstance(nav_item, list):
        # Adds a new item into existing sub-navigation
        nav_item.append(sub_name)
    else:
        # Adds a new sub-navigation
        urls.nav_order.insert(idx + 1, [sub_name])


def create_nav():
    """
    Creates the navigation context and sends a signal about this
    """
    orig_nav_order = urls.nav_order
    flat_nav_order = _flat_nav_order(orig_nav_order)

    nav_context = {
        app_name: _nav_links(
            app_name,
            orig_nav_order if app_name in orig_nav_order else flat_nav_order
        )
        for app_name in flat_nav_order
    }
    # Navigation context is ready
    signals.nav_ready.send(
        sender=None,  # not specified
        template='navigation/base_with_nav.html',
        context=nav_context
    )


def _flat_nav_order(nav_order):
    """
    list [a, [b, c], d, e, [f, g], h] -> itertools.chain [b, c, d, f, g, h]
    """
    (a, b) = tee(nav_order + [None])
    next(b, None)
    return list(chain.from_iterable([
        x if isinstance(x, list) else [x]
        for (x, y) in zip(a, b) if not isinstance(y, list)
    ]))


def _nav_links(app_name, nav_order):
    """
    list [a, *b*, c] -> dict {
        'backward_link': {link info of a}, 'forward_link': {link info of c}
    }
    """
    default_link = {}
    return {
        'backward_link': urls.nav_links.get(
            _backward_of(app_name, nav_order), default_link
        ),
        'forward_link': urls.nav_links.get(
            _forward_of(app_name, nav_order), default_link
        )
    }


def _backward_of(app_name, nav_order):
    """
    list [a, *b*, [c, d, e], f] -> a
    list [*a*, b, [c, d, e], f] -> f
    list [a, b, [c, d, e], *f*] -> b
    """
    idx = nav_order.index(app_name)
    # Searching of a first available app in front of specified app
    for i in range(1, len(nav_order)):
        prev_item = nav_order[idx - i]
        if not isinstance(prev_item, list) and prev_item in urls.nav_links:
            return prev_item
    # Otherwise
    return app_name


def _forward_of(app_name, nav_order):
    """
    list [*a*, b, [c, d, e], f] -> b
    list [a, *b*, [c, d, e], f] -> f
    list [a, b, [c, d, e], *f*] -> a
    """
    return _backward_of(app_name, nav_order[::-1])
