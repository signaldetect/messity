"""
Actions of the `reader` app
"""

from reader import models
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


def sample_books():
    """
    Samples all books and sends a signal about this
    """
    signals.books_sampled.send(
        sender=None,  # not specified
        books=all_books()
    )


def all_authors():
    """
    Returns all authors as a list of strings
    """
    return [str(author) for author in models.Author.objects.all()]


def all_books():
    """
    Returns all books as a list of strings
    """
    return [str(book) for book in models.Book.objects.all()]


def books_by_authors():
    """
    Returns books by authors as a list of tuples
    """
    def _books_of_author(author):
        """
        Returns books of specified author
        """
        return [str(book) for book in author.book_set.all()]

    return {
        str(author): _books_of_author(author)
        for author in models.Author.objects.all()
    }
