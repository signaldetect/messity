"""
URL configuration of the `messity` project
"""

from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls))
]

if 'navigation' in settings.INSTALLED_APPS:
    urlpatterns.append(url(r'^', include('navigation.urls')))
