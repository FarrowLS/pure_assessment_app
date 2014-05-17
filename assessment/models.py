# assessment/models.py

from django.db import models
# IMPORT USER INFO from django.db import models

from itembank.models import Itembank

"""
class Assessment(models.Model):
    itembank = models.ForeignKey(Itembank)
    # SHOULD I USE THIS OR USE django-model-utils INSTEAD? created = models.DateTimeField(auto_now_add=True)
    # USER RELATIONSHIP testee = models.[?]ForeignKey[?](settings.AUTH_USER_MODEL)
    # NUMBER OF ITEMS
    # NUMBER OF CORRECT ITEMS NEEDED TO PASS
"""

