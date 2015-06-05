"""
Views of the `reader` app
"""

from django.views.generic import TemplateView

from common.mixins import ContextMixin

from reader import actions


class HallView(ContextMixin, TemplateView):
    template_name = 'reader/hall.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'all_authors': actions.all_authors(),
            'all_books': actions.all_books(),
            'books_by_authors': actions.books_by_authors()
        })

        return context
