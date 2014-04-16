from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    def __unicode__(self):
        return self.title
