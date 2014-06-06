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
    # Rebuild as a CBV down the road

def item(request, testeeassessment_id):    
    current_testee_assessment = get_object_or_404(TesteeAssessment, pk=testeeassessment_id)
    if not current_testee_assessment.testee == request.user:
        raise PermissionDenied
    else:

        # get number of current answered items
        answered_items = TesteeResponse.objects.all().filter(testeeassessment=testeeassessment_id).exclude(option__isnull=True)
        # get number of items needed for assessment
        # compare these numbers to see if the assessment is complete - if necessary number are complete, mark assessment as complete and send to assessment index page
        if current_testee_assessment.assessment.itemsneeded <= len(answered_items):
            number_of_correct_items = TesteeResponse.objects.all().filter(testeeassessment=testeeassessment_id).filter(option__correct_answer=True)
            if len(number_of_correct_items) >= current_testee_assessment.assessment.itemsneededtopass:
                current_testee_assessment.status = 'passed'
            else:
                current_testee_assessment.status = 'failed'
            current_testee_assessment.save() 
            return HttpResponse('You are done!')
            # return HttpResponseRedirect(reverse('assessmentindex',))        


        unanswered_items = TesteeResponse.objects.all().filter(testeeassessment=testeeassessment_id).filter(option__isnull=True) 
        if len(unanswered_items) > 0:
            item = get_object_or_404(Item, pk=unanswered_items[0].item_id) 
            testee_response_id = unanswered_items[0].id


            # START TESTING
            # answered_and_unanswered_items = TesteeResponse.objects.all().filter(testeeassessment=testeeassessment_id)
            # answered_and_unanswered_items_ids = []
            # for an_item in answered_and_unanswered_items:
            #     answered_and_unanswered_items_ids.extend([an_item.item_id])
            # END TESTING


        else: 
            # Add try/except here
            current_items = Item.objects.all().filter(itembank = current_testee_assessment.assessment.itembank).filter(status='active')
            # Make sure item has not been presented before - NEEDS TO BE UPDATED
            item_approved = False            
            answered_and_unanswered_items = TesteeResponse.objects.all().filter(testeeassessment=testeeassessment_id) 
            answered_and_unanswered_items_ids = []
            for an_item in answered_and_unanswered_items:
                answered_and_unanswered_items_ids.extend([an_item.item_id])

            # More items in assessment than in itembank issue to be delt with later 
            
            random_item_position = random.randint(0, len(current_items) - 1)         
            item = current_items[random_item_position]        
           
            # Refactor this ugly hack - turn the selection code above into a function  
            if item.id in answered_and_unanswered_items_ids:
                return HttpResponseRedirect(reverse('assessmentitem', args=(testeeassessment_id,))) 
    
            new_testee_response = TesteeResponse(testeeassessment=current_testee_assessment, item=item, option=None) 
            new_testee_response.save()        
            testee_response_id = new_testee_response.id

        context = {'item': item,
                   'testee_response_id': testee_response_id,}
                   # 'testdata1': answered_and_unanswered_items_ids,}      

        return render(request, 'assessment/item.html', context)
        # Rebuild as a CBV down the road
        
def response(request, testee_response_id):
    current_testee_response = get_object_or_404(TesteeResponse, pk=testee_response_id)
    try:
        selected_option = Option.objects.get(pk=request.POST['option']) 
    except (KeyError, Option.DoesNotExist):

        # FOR TESTING - TO BE REMOVED
        """
        item = get_object_or_404(Item, pk=current_testee_response.item_id)
        context = {'item': item, 
                   'error_messge': "Please select an answer."} 
        return render(request, 'assessment/item.html', context)
        """
        # FOR TESTING - TO BE REMOVED

        return HttpResponseRedirect(reverse('assessmentitem', args=(current_testee_response.testeeassessment_id,))) 

    else:
        current_testee_response.option_id = selected_option.id
        current_testee_response.save()

        """
        # MOVING COMPLETION CHECK TO BEGINING OF ITEM DISPLAY ABOVE 
        number_of_completed_items = TesteeResponse.objects.all().filter(testeeassessment=current_testee_response.testeeassessment).exclude(option__isnull=True)
        current_assessment = get_object_or_404(Assessment, current_testee_response.testeeassessment.assessment_id)
        """

        # if current_assessment.itemsneeded >= len(number_of_completed_items):
        #     return HttpResponseRedirect(reverse('assessmentindex'))        

        # REMOVE THIS NOTE - CHECK TO SEE IF ASSESSMENT IS FINISHED 

        # return HttpResponse(current_assessment.itemsneeded)
        return HttpResponseRedirect(reverse('assessmentitem', args=(current_testee_response.testeeassessment_id,)))
