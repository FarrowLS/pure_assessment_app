from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import PermissionDenied
import random

from itembank.models import Item
from assessment.models import TesteeAssessment

def index(request):
    active_assesments_list = TesteeAssessment.objects.all().filter(testee=request.user).exclude(status='passed').exclude(status='failed') 
    finished_assesments_list = TesteeAssessment.objects.all().filter(testee=request.user).exclude(status='not-started').exclude(status='started') 
    context = {'active_assesments_list': active_assesments_list, 
               'finished_assesments_list': finished_assesments_list,}  
    return render(request, 'assessment/index.html', context)
    # Rebuild as a CBV down the road

def item(request, testeeassessment_id):
    current_testee_assessment = get_object_or_404(TesteeAssessment, pk=testeeassessment_id)
    if not current_testee_assessment.testee == request.user:
        raise PermissionDenied
    else:

        # TEST TO SEE IF THERE IS A TesteeResponse WITH NO SET option. IF SO SERVE THAT ITEM

        # Add try/except here
        current_items = Item.objects.all().filter(itembank = current_testee_assessment.assessment.itembank)
        random_item_position = random.randint(0, len(current_items) - 1) 
        item = current_items[random_item_position]
        context = {'item': item,}

        # CREATE NEW TesteeResponse WITH NO SET option

        return render(request, 'assessment/item.html', context)
        # Rebuild as a CBV down the road
        
def response(request):
    return HttpResponse("You are at an assessment item response page!")
