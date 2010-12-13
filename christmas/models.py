# -*- coding: utf-8 -*-
from django.db import models


class ChristmasGIF(models.Model):
    date = models.DateField()
    url_to_gif = models.URLField()
    
    
    def as_html(self):
        return "<img src=\"%s\" alt=\"%s\" />" % (self.url_to_gif, self.url_to_gif)
    as_html.allow_tags = True
    
    def gift_text(self):
        return u"þessa mynd!"
    
    def __unicode__(self):
        return "%s - %s" % (self.date, self.url_to_gif)
        
class ChristmasVideo(models.Model):
    date = models.DateField()
    title = models.CharField(max_length = 200)
    videoID = models.CharField(max_length = 200)
    
    def as_html(self):
        return """<div class="video"><object width="480" height="385">
                        <param name="movie" value="http://www.youtube.com/v/%s?fs=1&amp;hl=en_US"></param>
                        <param name="allowFullScreen" value="true"></param>
                        <param name="allowscriptaccess" value="always"></param>
                        <embed src="http://www.youtube.com/v/%s?fs=1&amp;hl=en_US" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="480" height="385"></embed>
                    </object></div>""" % (self.videoID, self.videoID)
    as_html.allow_tags = True
    
    def __unicode__(self):
        return "%s - %s" % (self.date, self.title)
        
    def gift_text(self):
        return u"þetta myndskeið!"