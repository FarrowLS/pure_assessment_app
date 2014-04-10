from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
