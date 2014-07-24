from django.db import models

from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField
from model_utils import Choices

class Itembank(TimeStampedModel):
    name = models.CharField(max_length=200)
    STATUS = Choices('active', 'inactive')
    status = StatusField()
    def __unicode__(self):
        return self.name 

class Item(TimeStampedModel):
    itembank = models.ForeignKey(Itembank)
    stem_text = models.CharField(max_length=200)
    feedback_text = models.TextField(default='')
    STATUS = Choices('active', 'inactive')
    status = StatusField()
    # stem_text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.stem_text

class Option(models.Model):
    item = models.ForeignKey(Item)
    option_text = models.CharField(max_length=200)
    correct_answer = models.BooleanField(default=False)
    def __unicode__(self):
        return self.option_text
