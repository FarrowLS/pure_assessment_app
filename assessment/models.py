from django.conf import settings
from django.db import models
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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
    def statusupdate(self, current_testee_assessment):
        # Check to see if testee has answered enough questions to complete the assessment
        answered_items = TesteeResponse.objects.all().filter(testeeassessment=current_testee_assessment.id).exclude(option__isnull=True)
        if not (current_testee_assessment.status == 'started'):
            current_testee_assessment.status = 'started'
            current_testee_assessment.save()
        if len(answered_items) >= current_testee_assessment.assessment.itemsneeded:
            # Since the testee has answered enough questions, check to see if testee has passed or failed
            number_of_correct_items = TesteeResponse.objects.all().filter(testeeassessment=current_testee_assessment.id).filter(option__correct_answer=True)
            if len(number_of_correct_items) >= current_testee_assessment.assessment.itemsneededtopass:
                current_testee_assessment.status = 'passed'
            else:
                current_testee_assessment.status = 'failed'
            current_testee_assessment.save()
    

class TesteeResponse(TimeStampedModel):
    testeeassessment = models.ForeignKey(TesteeAssessment)
    item = models.ForeignKey(Item)
    option = models.ForeignKey(Option, null=True, blank=True) 

