from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

# from item.models 

def index(request):
    # return HttpResponse("You're here on the items index page!")
    index_text = "The list of item banks goes here"
    context = {'bodytext': index_text,}
    return render(request, 'item/index.html', context) 
