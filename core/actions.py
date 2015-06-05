"""
Actions of the `core` app
"""

from core import signals


def launch():
    """
    Launches the `core` app and sends a signal about this
    """
    signals.app_link_ready.send(
        sender=None,  # not specified
        base_pattern=r'^',
        url_name='core:welcome',
        text='Go to Welcome page'
    )
    # Core app is ready
    signals.launched.send(sender=None)
