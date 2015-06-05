"""
Django Admin configuration of the `reader` app
"""

from django.contrib import admin

from reader import models


admin.site.register(models.Author)
admin.site.register(models.Book)
