from django.db import models

class Itembank(models.Model):
    name = models.CharField(max_length=200)

