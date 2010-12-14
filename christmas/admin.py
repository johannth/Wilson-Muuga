# -*- coding: utf-8 -*-

from django.contrib import admin

from christmas.models import ChristmasGIF, ChristmasVideo
from christmas.models import ChristmasPoem, ChristmasPoemHalf, ChristmasPoem2SecondHalf

class ChristmasGIFAdmin(admin.ModelAdmin):
    display_list = ("date", "as_html")

class ChristmasVideoAdmin(admin.ModelAdmin):
    display_list = ("date", "title")
    

admin.site.register(ChristmasGIF, ChristmasGIFAdmin)
admin.site.register(ChristmasVideo, ChristmasVideoAdmin)
admin.site.register(ChristmasPoem)
admin.site.register(ChristmasPoemHalf)
admin.site.register(ChristmasPoem2SecondHalf)