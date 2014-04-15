# about/views.py
# For FBV
from django.http import HttpResponse  
# from django.template import RequestContext, loader
# For CBV
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

import re

from about.models import Page

def index(request):
    raw_about_text = open("README", "r")
    about_text = raw_about_text.read()
    context = {'text2': about_text,}
    return render(request, 'about/index.html', context)    
    # return render(request, 'base.html', context)
    # return HttpResponse('Hi!')

# old FBV detail view
# def detail(request, page_id):
#     return HttpResponse('test - viewing page_id %s' % page_id)

class DetailView(generic.DetailView):
    model = Page
