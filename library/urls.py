#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.staticfiles import views as static_views
from django.conf.urls.static import static
from django.conf import settings

import library.views as views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^static/(?P<path>.*)$", static_views.serve, name="static"),
    url(r"^book/detail$", views.book_detail, name="book_detail"),
    url(r"^search/", views.book_search, name="book_search"),
    url(r"^about/", views.about, name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
