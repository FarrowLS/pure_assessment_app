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
        # FINISH TESTS FOR THIS
        # Select an item, make sure item has not been presented before and return it      
        answered_and_unanswered_items = TesteeResponse.objects.all().filter(testeeassessment=self.id) 
        answered_and_unanswered_items_ids = []

        for an_item in answered_and_unanswered_items:
            answered_and_unanswered_items_ids.extend([an_item.item_id])  

        def get_random_item(current_items):
            random_item_position = random.randint(0, len(current_items) - 1)         
            item = current_items[random_item_position]  
            if item.id in answered_and_unanswered_items_ids:  
                return get_random_item(current_items)
            else:
                return item

        item = get_random_item(current_items)   

        return item      
    
class TesteeResponse(TimeStampedModel):
    testeeassessment = models.ForeignKey(TesteeAssessment)
    item = models.ForeignKey(Item)
    option = models.ForeignKey(Option, null=True, blank=True) 

