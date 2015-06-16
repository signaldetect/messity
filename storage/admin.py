"""
Django Admin configuration of the `storage` app
"""

from django.contrib import admin

from storage import models


admin.site.register(models.Author)
admin.site.register(models.Book)
