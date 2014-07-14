from django.core.urlresolvers import reverse
from rest_framework import status

from django.contrib.auth.models import User
from django.test.client import Client

from rest_framework.test import APITestCase

from itembank.models import Itembank, Item, Option
# from assessment.models import Assessment, TesteeAssessment, TesteeResponse

# CURRENTLY ITEMBANK API IS FOR EXPERIMENTAL PURPOSES ONLY AND IS NOT BEING TESTED

class ItembankAPI(APITestCase):

    def setUp(self):
        pass