from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
import random

from itembank.models import Item
from assessment.models import TesteeAssessment, TesteeResponse

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
        unanswered_items = TesteeResponse.objects.all().filter(testeeassessment=testeeassessment_id).filter(option__isnull=True) 
        if len(unanswered_items) > 0:
            item = get_object_or_404(Item, pk=unanswered_items[0].item_id) # get_object_or_404(Poll, pk=poll_id)
            testee_response_id = unanswered_items[0].id        
        else:       
            # Add try/except here
            current_items = Item.objects.all().filter(itembank = current_testee_assessment.assessment.itembank)
            random_item_position = random.randint(0, len(current_items) - 1)         
            item = current_items[random_item_position]        
            new_testee_response = TesteeResponse(testeeassessment=current_testee_assessment, item=item, option=None) 
            new_testee_response.save()        
            testee_response_id = new_testee_response.id
        context = {'item': item,
                   'testee_response_id': testee_response_id}      
        return render(request, 'assessment/item.html', context)
        # Rebuild as a CBV down the road
        
def response(request, testee_response_id):
    return HttpResponse(request.POST['option'])
