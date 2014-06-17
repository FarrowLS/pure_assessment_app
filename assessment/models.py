from django.conf import settings
from django.db import models
import random

from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField
from model_utils import Choices 

from itembank.models import Itembank, Item, Option

class Assessment(TimeStampedModel):
    itembank = models.ForeignKey('itembank.Itembank')
    name = models.CharField(max_length=200)
    itemsneeded = models.IntegerField('number of items in assessment', default = 1) 
    itemsneededtopass = models.IntegerField('number of items needed to pass the assessment', default = 1)
    STATUS = Choices('active', 'inactive')
    status = StatusField()
    def __unicode__(self):
        return self.name

class TesteeAssessment(TimeStampedModel):
    assessment = models.ForeignKey(Assessment)
    testee = models.ForeignKey(settings.AUTH_USER_MODEL)
    STATUS = Choices('not-started', 'started', 'passed', 'failed')
    status = StatusField()
    def __unicode__(self):
        return self.assessment.name
    def status_update(self):
        # WRITE TESTS FOR THIS
        # Check to see if testee has answered enough questions to complete the assessment
        answered_items = TesteeResponse.objects.all().filter(testeeassessment=self.id).exclude(option__isnull=True)
        if not (self.status == 'started'):
            self.status = 'started'
            self.save()
        if len(answered_items) >= self.assessment.itemsneeded:
            # Since the testee has answered enough questions, check to see if testee has passed or failed
            number_of_correct_items = TesteeResponse.objects.all().filter(testeeassessment=self.id).filter(option__correct_answer=True)
            if len(number_of_correct_items) >= self.assessment.itemsneededtopass:
                self.status = 'passed'
            else:
                self.status = 'failed'
            self.save()
        return self.status
    def select_item(self, current_items):
        # Make sure item has not been presented before       

        # TEST THIS CODE TO SEE IF IT WILL GET 1 RANDOM ITEM FROM DB: objects.all().filter(isnull=True).filter('?')[:1]

        answered_and_unanswered_items = TesteeResponse.objects.all().filter(testeeassessment=self.id) 
        answered_and_unanswered_items_ids = []

        for an_item in answered_and_unanswered_items:
            answered_and_unanswered_items_ids.extend([an_item.item_id])  

        # THIS IS CURRENTLY BROKEN AND NEEDS TO BE FIXED
        
        random_item_position = random.randint(0, len(current_items) - 1)         
        item = current_items[random_item_position]    

        if item.id in answered_and_unanswered_items_ids or item == None:
            self.select_item(current_items)

            # select_random_item(current_items, answered_and_unanswered_items_ids)
            
        
        # item = select_random_item(current_items, answered_and_unanswered_items_ids)



        # Create a new TesteeResponse
        # new_testee_response = TesteeResponse(testeeassessment=self, item=item, option=None) 
        # new_testee_response.save()        
        # testee_response_id = new_testee_response.id
        

        return item #, testee_response_id      
    
class TesteeResponse(TimeStampedModel):
    testeeassessment = models.ForeignKey(TesteeAssessment)
    item = models.ForeignKey(Item)
    option = models.ForeignKey(Option, null=True, blank=True) 

