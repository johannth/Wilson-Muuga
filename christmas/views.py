# -*- coding: utf-8 -*-
from datetime import date

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.http import HttpResponseRedirect

from christmas.models import ChristmasGIF, ChristmasVideo, ChristmasPoem, ChristmasPoemHalf, ChristmasPoem2SecondHalf

def save_second_half(request):
    poemID = int(request.POST["poemID"])
    poem = ChristmasPoem.objects.get(pk = poemID)
    
    half = ChristmasPoemHalf.objects.create(first_line = request.POST["first_line"],
                                second_line = request.POST["second_line"],
                                author = request.POST["author"])
    
    connection = ChristmasPoem2SecondHalf.objects.create(poem = poem,
                                                            second_half = half)
    
    return HttpResponseRedirect(reverse("gott-i-skoinn-date", kwargs = {'year': poem.date.year, 
                                                                            'month': poem.date.month, 
                                                                            'day': poem.date.day }))

def parse_date(date_string):
    if date_string:
        return date(int(date_string[:4]), int(date_string[5:7]), int(date_string[8:]))
    else:
        return None
        
def get_gift(today):
    gift = None
    for Class in [ChristmasGIF, ChristmasVideo, ChristmasPoem]:
        try:
            gift = Class.objects.get(date = today)
        except:
            continue
    
    return gift

def todays_gif(request, year = None, month = None, day = None):
    if year is None:
        today = date.today()
    else:
        today = date(int(year), int(month), int(day))
        
    previous_days = []
    
    real_today = date.today()
    for i in range(12, real_today.day + 1):
        previous_days.append(date(year = real_today.year, month = real_today.month, day = i))
    
            

    
    gift = get_gift(today)
        
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
    
    context = {'today': today, 
                'gift': gift, 
                'previous_days': previous_days,
                'santa_claus_name': santa_claus_names[today.day] }
    if gift:
        template = gift.get_template()
        context.update(gift.get_extra_context())
    else:
        template = "christmas.html"
    return render_to_response(template, context , context_instance = RequestContext(request))