from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500, default='')
    body = models.TextField()
    def __unicode__(self):
        return self.title
