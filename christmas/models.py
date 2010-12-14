# -*- coding: utf-8 -*-
from django.db import models
from django.template import Context
from django.template.loader import get_template
from django.forms import ModelForm

class ChristmasPoemHalf(models.Model):
    first_line = models.CharField(max_length = 500)
    second_line = models.CharField(max_length = 500)
    author = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return u"%s, %s - %s" % (self.first_line, self.second_line, self.author)
    
class ChristmasPoem2SecondHalf(models.Model):
    datetime_created = models.DateTimeField(auto_now_add = True)
    poem = models.ForeignKey("ChristmasPoem", related_name = "poem")
    second_half = models.ForeignKey(ChristmasPoemHalf, related_name = "second_half")
    
    class Meta:
        ordering = ["-datetime_created"]
        
    def __unicode__(self):
        return u"%s - %s" % (self.datetime_created, self.second_half)
    
class ChristmasPoem(models.Model):
    date = models.DateField()
    first_half = models.ForeignKey(ChristmasPoemHalf)
    
    def get_completed_poems(self):
        return ChristmasPoem2SecondHalf.objects.filter(poem = self)
        
    def get_template(self):
        return "poem_gift.html"
        
    def get_extra_context(self):
        return {"poem": self, "poems": self.get_completed_poems()}
        
    def gift_text(self):
        return u"þennan fyrripart!"
    




class ChristmasGIF(models.Model):
    date = models.DateField()
    url_to_gif = models.URLField()
    
    
    def as_html(self):
        return "<img src=\"s\" alt=\"%s\" />" % (self.url_to_gif, self.url_to_gif)
    as_html.allow_tags = True
    
    def get_template(self):
        return "poem_image.html"
        
    def get_extra_context(self):
        return {"url": self.url_to_gif}
    
    def gift_text(self):
        return u"þessa mynd!"
    
    def __unicode__(self):
        return "%s - %s" % (self.date, self.url_to_gif)
        
class ChristmasVideo(models.Model):
    date = models.DateField()
    title = models.CharField(max_length = 200)
    videoID = models.CharField(max_length = 200)
    
    def get_template(self):
        return "video_gift.html"
        
    def get_extra_context(self):
        return {"videoID": self.videoID }
    
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