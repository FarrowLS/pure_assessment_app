# from django.conf import settings
from django.db import models

from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices 

from itembank.models import Itembank

# REMOVE STATUSMODEL
class Assessment(TimeStampedModel, StatusModel):
    itembank = models.ForeignKey(Itembank)
    itemsneeded = models.IntegerField('number of items in assessment', default = 1) 
    itemsneededtopass = models.IntegerField('number of items needed to pass the assessment', default = 1)
    STATUS = Choices('active', 'inactive')
    # def __unicode__(self):
    #     return self.name

'''
class Assessment(TimeStampedModel, StatusModel):
    itembank = models.ForeignKey(Itembank)
    testee = models.OneToOneField(settings.AUTH_USER_MODEL)
    itemsneeded = models.IntegerField('number of items in assessment', default = 1)
    itemsneededtopass = models.IntegerField('number of items needed to pass the assessment', default = 1)
    STATUS = Choices('not-started', 'started', 'finished')
'''

