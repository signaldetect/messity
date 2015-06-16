"""
Handling signals of the `storage` app
"""

from django.dispatch import receiver

from storage import signals
from reader import views


@receiver(signals.authors_sampled)
def authors_sampled(sender, authors, **kwargs):
    views.HallView.all_authors = authors


@receiver(signals.books_sampled)
def books_sampled(sender, books, **kwargs):
    views.HallView.all_books = books


@receiver(signals.books_by_authors_sampled)
def books_by_authors_sampled(sender, books, **kwargs):
    views.HallView.books_by_authors = books
