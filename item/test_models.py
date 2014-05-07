from django.test import TestCase

from items.models import Itembank

def create_itembank(name):
    """
    Creates an itembank with a title
    """
    return Itembank.objects.create(name=name)

