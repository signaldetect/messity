"""
URL configuration of the `reader` app
"""

from django.conf.urls import url

from reader import views


urlpatterns = [
    url(r'^$', views.HallView.as_view()),
    url(r'^hall/', views.HallView.as_view(), name='hall')
]
