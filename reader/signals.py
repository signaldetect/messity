"""
Defining signals of the `reader` app
"""

from django.dispatch import Signal


app_link_ready = Signal(providing_args=['base_pattern', 'url_name', 'text'])

books_sampled = Signal(providing_args=['books'])
