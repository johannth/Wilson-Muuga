# -*- coding: utf-8 -*-
from datetime import date

from django.shortcuts import render_to_response
from django.template.context import RequestContext

from christmas.models import ChristmasGIF

def parse_date(date_string):
    if date_string:
        return date(int(date_string[:4]), int(date_string[5:7]), int(date_string[8:]))
    else:
        return None

def todays_gif(request):
    today = parse_date(request.GET.get("today", "")) or date.today()
    try:
        gif = ChristmasGIF.objects.get(date = today)
    except:
        gif = None
        
    santa_claus_names = {
        12: "Stekkjastaur",
        13: "Giljagaur",
        14: "Stúfur",
        15: "Þvörusleikir",
        16: "Pottaskefilr",
        17: "Askasleikir",
        18: "Hurðaskellir",
        19: "Skyrgámur",
        20: "Bjúgnakrækir",
        21: "Gluggagægir",
        22: "Gáttaþefur",
        23: "Ketkrókur",
        24: "Kertasníkir" }
    
    return render_to_response("christmas.html", {'gif': gif, 'santa_claus_name': santa_claus_names[today.day] }, context_instance = RequestContext(request))