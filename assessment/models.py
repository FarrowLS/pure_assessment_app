from django.conf import settings
from django.db import models

from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField
from model_utils import Choices 

from itembank.models import Itembank

class Assessment(TimeStampedModel):
    itembank = models.ForeignKey('itembank.Itembank')
    name = models.CharField(max_length=200)
    itemsneeded = models.IntegerField('number of items in assessment', default = 1) 
    itemsneededtopass = models.IntegerField('number of items needed to pass the assessment', default = 1)
    STATUS = Choices('active', 'inactive')
    status = StatusField()
    def __unicode__(self):
        return self.name

'''
class Assessment(TimeStampedModel, StatusModel):
    itembank = models.ForeignKey(Itembank)
    testee = models.OneToOneField(settings.AUTH_USER_MODEL)
    itemsneeded = models.IntegerField('number of items in assessment', default = 1)
    itemsneededtopass = models.IntegerField('number of items needed to pass the assessment', default = 1)
    STATUS = Choices('not-started', 'started', 'finished')
'''

