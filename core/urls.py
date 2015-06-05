"""
URL configuration of the `core` app
"""

from django.conf.urls import url

from core import views


urlpatterns = [
    url(r'^$', views.WelcomeView.as_view()),
    url(r'^welcome/', views.WelcomeView.as_view(), name='welcome')
]
