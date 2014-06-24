from django.test import TestCase
from django.contrib.auth.models import User

from itembank.models import Itembank, Item, Option
from assessment.models import Assessment, TesteeAssessment, TesteeResponse


class TesteeAssessmentMethodtests(TestCase):

    def setUp(self):
        self.test_itembank1 = Itembank.objects.create(name="Itembank1")
        self.test_assessment1 = Assessment.objects.create(name="Test1", itembank=self.test_itembank1)
        # Setup for items and their options
        self.test_item1 = Item.objects.create(itembank=self.test_itembank1, stem_text="Test stem text1")
        self.test_option1_1 = Option.objects.create(item=self.test_item1, option_text="True", correct_answer=True)
        self.test_option1_2 = Option.objects.create(item=self.test_item1, option_text="False", correct_answer=False)
        self.test_item2 = Item.objects.create(itembank=self.test_itembank1, stem_text="Test stem text2")
        self.test_option2_1 =  Option.objects.create(item=self.test_item2, option_text="True", correct_answer=True)
        self.test_option2_2 = Option.objects.create(item=self.test_item2, option_text="False", correct_answer=False)
        # Setup for users and user assessments
        self.test_user_setup1 = User.objects.create_user(username='bob', password='secret')
        # self.test_user_setup2 = User.objects.create_user(username='joe', password='secret')
        self.test_userassessment1 = TesteeAssessment.objects.create(assessment=self.test_assessment1, testee=self.test_user_setup1)
        # I AM HERE!!!

    def tearDown(self):
        pass

    def test_status_update_returns_started(self):
        """
        status_update() should return 'started' when an assessment is begun but not finished 
        """
        pass
        

# Write tests for status_update()

# Write tests for select_item()
