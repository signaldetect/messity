"""
Common mixins
"""


class ContextMixin(object):
    """
    Helps to extend a base template with an extra context
    """
    template_base = 'base.html'
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({'template_base': self.template_base})
        context.update(self.extra_context)

        return context
