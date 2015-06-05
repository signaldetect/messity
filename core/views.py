"""
Views of the `core` app
"""

from django.views.generic import TemplateView

from common.mixins import ContextMixin


class WelcomeView(ContextMixin, TemplateView):
    template_name = 'core/welcome.html'
