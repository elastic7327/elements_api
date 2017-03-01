#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from engine import views

urlpatterns = patterns(
    '', url(r'^csv/$', views.CsvList.as_view()),
    url(r'^csv/download/$', views.ExportView.as_view()),
    url(r'^csv/(?P<pk>[0-9]+)/$', views.CsvDetail.as_view()),
    url(r'^content/$', views.ContentList.as_view()),
    url(r'^content/(?P<pk>[0-9]+)/$', views.ContentDetail.as_view()),)

#format_suffix_patterns for django-restframework
urlpatterns = format_suffix_patterns(urlpatterns)
