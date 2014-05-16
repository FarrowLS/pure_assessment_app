"""
NOT IN USE - COMMENTED OUT
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

from itembank.models import Itembank

def index(request):
    itembank_list = Itembank.objects.order_by('name')
    context = {'itembank_list': itembank_list,}
    return render(request, 'item/index.html', context)
""" 
