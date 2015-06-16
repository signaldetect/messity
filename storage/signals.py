"""
Defining signals of the `storage` app
"""

from django.dispatch import Signal


authors_sampled = Signal(providing_args=['authors'])

books_sampled = Signal(providing_args=['books'])

books_by_authors_sampled = Signal(providing_args=['books'])
