from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from django.contrib import messages
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
    # Check to see if the user has access to the test
    if not current_testee_assessment.testee == request.user:
        raise PermissionDenied
    else:
        
        # If a form is being submitted, process it and redirect back to the form
        if request.method == 'POST':
            current_testee_response = get_object_or_404(TesteeResponse, pk=request.POST['TesteeResponse'])
            try:
                selected_option = Option.objects.get(pk=request.POST['option']) 
            except (KeyError, Option.DoesNotExist):
                messages.add_message(request, messages.INFO, 'There was no valid answer submitted for the last question. Please answer the question below.')
                return HttpResponseRedirect(reverse('assessmentitem', args=(current_testee_response.testeeassessment_id,))) 
            else:
                current_testee_response.option_id = selected_option.id
                current_testee_response.save()       
                return HttpResponseRedirect(reverse('assessmentitem', args=(current_testee_response.testeeassessment_id,)))
        
        # If a form is not being submitted, serve the form
        else:    
            # Check to see if assessment is finished - if it is, determine if the testee passed or failed 
            current_testee_assessment.status_update()    
            if current_testee_assessment.status == 'passed' or current_testee_assessment.status == 'failed':
                messages.add_message(request, messages.INFO, 'You have finished your %s test!' % current_testee_assessment.assessment.name)
                return HttpResponseRedirect(reverse('assessmentindex',))

            # Check to see if testee has unanswered items - if so, serve the first one
            unanswered_items = TesteeResponse.objects.all().filter(testeeassessment=testeeassessment_id).filter(option__isnull=True)
            if len(unanswered_items) > 0:
                item = get_object_or_404(Item, pk=unanswered_items[0].item_id) 
                testee_response_id = unanswered_items[0].id

            # If there is not an existing item, serve a new item
            else:   
                #Select a new item - make sure it is from the correct itembank 
                current_items = Item.objects.all().filter(itembank = current_testee_assessment.assessment.itembank).filter(status='active')

                if len(current_items) < current_testee_assessment.assessment.itemsneeded:
                    # Need to include an error message with this redirect - Inform use there is an issue with the test and to contact the admin
                    messages.add_message(request, messages.INFO, 'There are not enough questions in your test. Please contact your tester.')
                    return HttpResponseRedirect(reverse('assessmentindex',))
                else: 
                    # Get the item
                    item = current_testee_assessment.select_item(current_items)

                    # Create a new TesteeResponse
                    new_testee_response = TesteeResponse(testeeassessment=current_testee_assessment, item=item, option=None) 
                    new_testee_response.save()        
                    testee_response_id = new_testee_response.id

            current_options = sorted(Option.objects.all().filter(item=item.id), key=lambda x: random.random())            

            context = {'item': item,
                       'current_options': current_options, 
                       'testeeassessment_id': current_testee_assessment.id,  
                       'testee_response_id': testee_response_id,}
                       
            return render(request, 'assessment/item.html', context)     
