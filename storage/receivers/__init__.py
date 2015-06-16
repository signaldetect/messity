"""
Handling signals of the `storage` app
"""

from django.dispatch import receiver
from django.db.models import signals

from storage import models
from storage import actions


@receiver(signals.post_save, sender=models.Author)
def author_saved(sender, **kwargs):
    actions.sample_authors()


@receiver(signals.post_save, sender=models.Book)
def book_saved(sender, **kwargs):
    actions.sample_books()
