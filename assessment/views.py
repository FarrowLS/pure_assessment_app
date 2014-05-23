from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from assessment.models import TesteeAssessment

def index(request):
    active_assesments_list = TesteeAssessment.objects.all().exclude(status='passed').exclude(status='failed') 
    finished_assesments_list = TesteeAssessment.objects.all().exclude(status='not-started').exclude(status='started') 
    context = {'active_assesments_list': active_assesments_list, 
               'finished_assesments_list': finished_assesments_list,}  
    return render(request, 'assessment/index.html', context)
    # return HttpResponse("You are at assessment index!")
