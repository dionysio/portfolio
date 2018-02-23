#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.decorators.cache import cache_page
from base import views

urlpatterns = [
    url(r'^contact/$', views.ContactUs.as_view(), name='contact'),

    url(r'^$', views.HomeView.as_view(), name='index')
]
