"""
Defining signals of the `core` app
"""

from django.dispatch import Signal


app_link_ready = Signal(providing_args=['base_pattern', 'url_name', 'text'])

launched = Signal(providing_args=[])
