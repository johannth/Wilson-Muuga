# -*- coding: utf-8 -*-

from django.contrib import admin

from christmas.models import ChristmasGIF

class ChristmasGIFAdmin(admin.ModelAdmin):
    display_list = ("date", "as_html")

admin.site.register(ChristmasGIF, ChristmasGIFAdmin)