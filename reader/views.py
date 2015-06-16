"""
Views of the `reader` app
"""

from django.views.generic import TemplateView

from common.mixins import ContextMixin

from reader import actions


class HallView(ContextMixin, TemplateView):
    template_name = 'reader/hall.html'

    all_authors = None
    all_books = None
    books_by_authors = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'all_authors': self.all_authors,
            'all_books': self.all_books,
            'books_by_authors': self.books_by_authors
        })

        return context
