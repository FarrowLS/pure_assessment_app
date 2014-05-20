from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from assessment.models import Assessment

def index(request):
    active_assesments_list = Assessment.objects.all().exclude(status='inactive')
    finished_assesments_list = Assessment.objects.all().filter(status='inactive')
    context = {'active_assesments_list': active_assesments_list, 
               'finished_assesments_list': finished_assesments_list,}  
    return render(request, 'assessment/index.html', context)
    # return HttpResponse("You are at assessment index!")
