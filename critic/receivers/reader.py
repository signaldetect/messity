"""
Handling signals of the `reader` app
"""

from django.dispatch import receiver

from reader import signals
from critic import forms


@receiver(signals.books_sampled)
def books_sampled(sender, books, **kwargs):
    forms.ReviewForm.declared_fields['book'].choices = (
        (book, book) for book in books
    )
