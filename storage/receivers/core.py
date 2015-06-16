"""
Handling signals of the `core` app
"""

from django.dispatch import receiver
from django.db.utils import OperationalError

from core import signals
from storage import actions


@receiver(signals.launched)
def launched(sender, **kwargs):
    actions.sample_authors()
    actions.sample_books()
    actions.sample_books_by_authors()
