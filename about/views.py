from django.http import HttpResponse
# from django.template import RequestContext, loader

import re

from django.shortcuts import render

# raw_about_text = open("README", "r")
# about_text = raw_about_text.read()

def index(request):
    raw_about_text = open("README", "r")
    about_text = raw_about_text.read()
    context = {'text2': about_text,}
    return render(request, 'about/index.html', context)    
    # return render(request, 'base.html', context)
    # return HttpResponse('Hi!')

def detail(request, page_id):
    return HttpResponse('test')
