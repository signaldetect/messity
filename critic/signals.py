"""
Defining signals of the `critic` app
"""

from django.dispatch import Signal


app_link_ready = Signal(providing_args=['base_pattern', 'url_name', 'text'])

sub_link_ready = Signal(providing_args=['url_name', 'text', 'alias'])

sub_button_ready = Signal(providing_args=['button_type', 'text', 'alias'])
