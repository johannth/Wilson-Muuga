# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class ChristmasGIF(models.Model):
    date = models.DateField()
    url_to_gif = models.URLField()
    
    
    def as_html(self):
        return "<img src=\"%s\" alt=\"%s\" />" % (self.url_to_gif, self.url_to_gif)
    as_html.allow_tags = True
    
    def __unicode__(self):
        return "%s - %s" % (self.date, self.url_to_gif)