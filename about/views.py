# about/views.py
# For FBV
from django.http import HttpResponse  
# from django.template import RequestContext, loader
# For CBV
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
# General includes
import re

from about.models import Page

from django.contrib.auth import logout

def index(request):
    raw_about_text = open("README", "r")
    about_text = raw_about_text.read()
    if request.user.is_authenticated():
        loggedinstatus = 'User is logged in'
    else:
        loggedinstatus = 'User is not logged in'
    context = {'text1': loggedinstatus, 'text2': about_text,}
    return render(request, 'about/index.html', context)    
   
class DetailView(generic.DetailView):
    model = Page
