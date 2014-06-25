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

# For testing if user is authenticated
# if request.user.is_authenticated():

def index(request):
    raw_about_text = open("README", "r")
    about_text = raw_about_text.read()
    about_page_list = Page.objects.order_by('title') 
    context = {'text1': about_text, 'text2': about_page_list,}
    return render(request, 'about/index.html', context)    
   
class DetailView(generic.DetailView):
    model = Page
