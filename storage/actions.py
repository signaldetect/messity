"""
Actions of the `storage` app
"""

from django.db import connection

from storage import models
from storage import signals


def sample_authors():
    """
    Samples all authors and sends a signal about this
    """
    signals.authors_sampled.send(
        sender=None,  # not specified
        authors=all_authors()
    )


def sample_books():
    """
    Samples all books and sends a signal about this
    """
    signals.books_sampled.send(
        sender=None,  # not specified
        books=all_books()
    )


def sample_books_by_authors():
    """
    Samples books by authors and sends a signal about this
    """
    signals.books_by_authors_sampled.send(
        sender=None,  # not specified
        books=books_by_authors()
    )


def all_authors():
    """
    Returns all authors as a list of strings
    """
    if _db_table_exists(models.Author):
        return [str(author) for author in models.Author.objects.all()]
    # Otherwise
    return []


def all_books():
    """
    Returns all books as a list of strings
    """
    if _db_table_exists(models.Book):
        return [str(book) for book in models.Book.objects.all()]
    # Otherwise
    return []


def books_by_authors():
    """
    Returns books by authors as a dict of pairs `<author>: <author's-books>`
    """
    def _books_of_author(author):
        """
        Returns books of specified author
        """
        return [str(book) for book in author.book_set.all()]

    if _db_table_exists(models.Author):
        return {
            str(author): _books_of_author(author)
            for author in models.Author.objects.all()
        }
    # Otherwise
    return {}


def _db_table_exists(model):
    """
    Checks that DB table of specified model is exist
    """
    return model._meta.db_table in connection.introspection.table_names()
