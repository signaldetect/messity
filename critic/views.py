"""
Views of the `critic` app
"""

from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

from common.mixins import ContextMixin

from critic import forms
from critic import actions


class ReviewView(ContextMixin, FormView):
    form_class = forms.ReviewForm
    template_name = 'critic/review.html'

    def get_success_url(self):
        return reverse('critic:thanks')

    def form_valid(self, form):
        actions.send_review(
            book_name=form.cleaned_data.get('book', None),
            review_text=form.cleaned_data.get('text', None)
        )
        return super().form_valid(form)


class ThanksView(ContextMixin, TemplateView):
    template_name = 'critic/thanks.html'
