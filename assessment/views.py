from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from itembank.models import Item
from assessment.models import TesteeAssessment

# REBUILD AS CBV
def index(request):
    active_assesments_list = TesteeAssessment.objects.all().filter(testee=request.user).exclude(status='passed').exclude(status='failed') 
    finished_assesments_list = TesteeAssessment.objects.all().filter(testee=request.user).exclude(status='not-started').exclude(status='started') 
    context = {'active_assesments_list': active_assesments_list, 
               'finished_assesments_list': finished_assesments_list,}  
    return render(request, 'assessment/index.html', context)

# REBUILD AS CBV
def item(request):
    # body_text = "You are at an assessment item page!"
    item = get_object_or_404(Item, pk=1)
    context = { # 'body_text': body_text,
               'item': item,}
    return render(request, 'assessment/item.html', context)

def response(request):
    return HttpResponse("You are at an assessment item response page!")
