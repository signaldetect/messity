"""
URL configuration of the `critic` app
"""

from django.conf.urls import url

from critic import views


urlpatterns = [
    url(r'^$', views.ReviewView.as_view()),
    url(r'^review/', views.ReviewView.as_view(), name='review'),
    url(r'^thanks/', views.ThanksView.as_view(), name='thanks')
]
