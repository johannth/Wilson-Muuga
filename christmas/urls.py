# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from christmas.views import todays_gif, save_second_half

urlpatterns = patterns('',
    url('gott-i-skoinn/$', todays_gif, name = "gott-i-skoinn"),
    url('gott-i-skoinn/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', todays_gif, name = "gott-i-skoinn-date"),
    url('vista-seinnipart/$', save_second_half, name = "save-second-half")
)