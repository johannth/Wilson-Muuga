# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from christmas.views import todays_gif

urlpatterns = patterns('',
    url('gott-i-skoinn/$', todays_gif, name = "gott-i-skoinn")
)