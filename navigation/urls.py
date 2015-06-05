"""
URL configuration of the `navigation` app
"""


urlpatterns = []

# {<app-name>: <url-pattern>}
app_urls = {}

# core <-> reader <-> critic <-> core
nav_order = ['core', 'reader', 'critic']

# {<app-name>: {'url': <reversed-url>, 'text': <link-text>, <<button_type>>}}
# <<button_type>> is optional and 'button_type': <'button'/'submit'/'reset'>
nav_links = {}
