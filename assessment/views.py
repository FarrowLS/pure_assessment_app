from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from assessment.models import TesteeAssessment

def index(request):
    active_assesments_list = TesteeAssessment.objects.all().exclude(status='passed').exclude(status='failed') 
    finished_assesments_list = TesteeAssessment.objects.all().exclude(status='not-started').exclude(status='started') 
    context = {'active_assesments_list': active_assesments_list, 
               'finished_assesments_list': finished_assesments_list,}  
    return render(request, 'assessment/index.html', context)

def item(request):
    body_text = "You are at an assessment item page!"
    # item = get_object_or_404()
    context = {'body_text': body_text}
    return render(request, 'assessment/item.html', context)
    # return HttpResponse("You are at an assessment item page!")
