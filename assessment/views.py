from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
import random

from itembank.models import Item, Option
from assessment.models import Assessment, TesteeAssessment, TesteeResponse

def index(request):
    active_assesments_list = TesteeAssessment.objects.all().filter(testee=request.user).exclude(status='passed').exclude(status='failed') 
    finished_assesments_list = TesteeAssessment.objects.all().filter(testee=request.user).exclude(status='not-started').exclude(status='started') 
    context = {'active_assesments_list': active_assesments_list, 
               'finished_assesments_list': finished_assesments_list,}  
    return render(request, 'assessment/index.html', context)

def item(request, testeeassessment_id):    
    current_testee_assessment = get_object_or_404(TesteeAssessment, pk=testeeassessment_id)
    if not current_testee_assessment.testee == request.user:
        raise PermissionDenied
    else:

        # if request.method == 'POST':

        # Check to see if testee is done - if they are set status
        answered_items = TesteeResponse.objects.all().filter(testeeassessment=testeeassessment_id).exclude(option__isnull=True)
        if len(answered_items) >= current_testee_assessment.assessment.itemsneeded:
            number_of_correct_items = TesteeResponse.objects.all().filter(testeeassessment=testeeassessment_id).filter(option__correct_answer=True)

            if len(number_of_correct_items) >= current_testee_assessment.assessment.itemsneededtopass:
                current_testee_assessment.status = 'passed'
            else:
                current_testee_assessment.status = 'failed'
            current_testee_assessment.save() 
            return HttpResponseRedirect(reverse('assessmentindex',))        

        # Check to see if testee has unanswered items
        unanswered_items = TesteeResponse.objects.all().filter(testeeassessment=testeeassessment_id).filter(option__isnull=True)
        if len(unanswered_items) > 0:
            item = get_object_or_404(Item, pk=unanswered_items[0].item_id) 
            testee_response_id = unanswered_items[0].id

        # Serve new item
        else: 
            ## START ITEM SELCTION
            # Add try/except here
            current_items = Item.objects.all().filter(itembank = current_testee_assessment.assessment.itembank).filter(status='active')

            # Make sure item has not been presented before - NEEDS TO BE UPDATED
            item_approved = False            

            # TEST THIS CODE TO SEE IF IT WILL GET 1 RANDOM ITEM FROM DB: objects.all().filter(isnull=True).filter('?')[:1]

            answered_and_unanswered_items = TesteeResponse.objects.all().filter(testeeassessment=testeeassessment_id) 
            answered_and_unanswered_items_ids = []

            for an_item in answered_and_unanswered_items:
                answered_and_unanswered_items_ids.extend([an_item.item_id])  

            # More items in assessment than in itembank issue to be delt with later 
            def select_random_item():
                random_item_position = random.randint(0, len(current_items) - 1)         
                item = current_items[random_item_position]        
                if item.id in answered_and_unanswered_items_ids:
                    select_random_item()
                return item
            
            item = select_random_item()

            # BEING REFACTORED OUT
            # random_item_position = random.randint(0, len(current_items) - 1)         
            # item = current_items[random_item_position] 
            # Refactor this ugly hack - turn the selection code above into a function 
 
            # if item.id in answered_and_unanswered_items_ids:
 	        # Add django.shortcuts.render here.
            #    return HttpResponseRedirect(reverse('assessmentitem', args=(testeeassessment_id,))) 
            ## END ITEM SELECTION

            new_testee_response = TesteeResponse(testeeassessment=current_testee_assessment, item=item, option=None) 
            new_testee_response.save()        
            testee_response_id = new_testee_response.id
        context = {'item': item,
                   'testee_response_id': testee_response_id,}
        return render(request, 'assessment/item.html', context)
        
def response(request, testee_response_id):
    # current_testee_response = get_object_or_404(TesteeResponse, pk=testee_response_id)
    current_testee_response = get_object_or_404(TesteeResponse, pk=request.POST['TesteeResponse'])
    try:
        selected_option = Option.objects.get(pk=request.POST['option']) 
    except (KeyError, Option.DoesNotExist):
        return HttpResponseRedirect(reverse('assessmentitem', args=(current_testee_response.testeeassessment_id,))) 
    else:
        current_testee_response.option_id = selected_option.id
        current_testee_response.save()       
        return HttpResponseRedirect(reverse('assessmentitem', args=(current_testee_response.testeeassessment_id,)))
