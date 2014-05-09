from django.db import models

class Itembank(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name 

class Item(models.Model):
    itembank = models.ForeignKey(Itembank)
    active = models.BooleanField(default=True)
    stem_text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.stem_text

class Option(models.Model):
    item = models.ForeignKey(Item)
    option_text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.option_text
