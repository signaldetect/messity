"""
Actions of the `reader` app
"""

from reader import signals


def create_app_link():
    """
    Creates a link to the `reader` app
    """
    signals.app_link_ready.send(
        sender=None,  # not specified
        base_pattern=r'^reader/',
        url_name='reader:hall',
        text='Go to Reader page'
    )
