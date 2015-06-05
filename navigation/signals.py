"""
Defining signals of the `navigation` app
"""

from django.dispatch import Signal


nav_ready = Signal(providing_args=['template', 'context'])
