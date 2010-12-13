# -*- coding: utf-8 -*-
from datetime import date

from django.shortcuts import render_to_response
from django.template.context import RequestContext

from christmas.models import ChristmasGIF, ChristmasVideo

def parse_date(date_string):
    if date_string:
        return date(int(date_string[:4]), int(date_string[5:7]), int(date_string[8:]))
    else:
        return None

def todays_gif(request, year = None, month = None, day = None):
    if year is None:
        today = date.today()
    else:
        today = date(int(year), int(month), int(day))
        
    previous_days = []
    
    for gift in ChristmasGIF.objects.all():
        gift_date = gift.date
        if gift_date not in previous_days and gift_date < date.today():
            previous_days.append(gift_date)
            
    for gift in ChristmasVideo.objects.all():
        gift_date = gift.date
        if gift_date not in previous_days and gift_date < date.today():
            previous_days.append(gift_date)
            
    previous_days.sort()
    
    try:
        gift = ChristmasGIF.objects.get(date = today)
    except:
        try:
            gift = ChristmasVideo.objects.get(date = today)
        except:
            gift = None
        
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
    
    return render_to_response("christmas.html", {'today': today, 
                                                    'gift': gift, 
                                                    'previous_days': previous_days,
                                                    'santa_claus_name': santa_claus_names[today.day] }, context_instance = RequestContext(request))