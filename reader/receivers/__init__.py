"""
Handling signals of the `reader` app
"""

from django.dispatch import receiver
from django.db.models import signals

from reader import models
from reader import actions


@receiver(signals.post_save, sender=models.Book)
def book_saved(sender, **kwargs):
    actions.sample_books()
