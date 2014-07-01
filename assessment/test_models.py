from django.test import TestCase
from django.contrib.auth.models import User

from itembank.models import Itembank, Item, Option
from assessment.models import Assessment, TesteeAssessment, TesteeResponse


class TesteeAssessmentMethodtests(TestCase):

    def setUp(self):
        self.test_itembank1 = Itembank.objects.create(name="Itembank1")
        self.test_assessment1 = Assessment.objects.create(name="Test1", itembank=self.test_itembank1, itemsneeded=2, itemsneededtopass=1)
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
        

    def tearDown(self):
        pass
   

    def test_status_update_returns_not_started(self):
        """
        A unstarted assessment should show as 'not-started'  
        """   
        self.assertEqual(self.test_userassessment1.status, 'not-started') 


    def test_status_update_returns_started(self):
        """
        status_update() should return 'started' when an assessment is begun but not finished 
        """
        current_status = self.test_userassessment1.status_update()
        self.assertEqual(current_status, 'started')
        
    def test_status_update_returns_failed(self):
        """
        status_update() should return 'failed' when an assessment is finished and not passed 
        """

        TesteeResponse.objects.create(testeeassessment=self.test_userassessment1, item=self.test_item1, option=self.test_option1_2)
        TesteeResponse.objects.create(testeeassessment=self.test_userassessment1, item=self.test_item2, option=self.test_option2_2)

        current_status = self.test_userassessment1.status_update()
        self.assertEqual(current_status, 'failed')

    def test_status_update_returns_passed(self):
        """
        status_update() should return 'passed' when an assessment is finished and passed 
        """
        TesteeResponse.objects.create(testeeassessment=self.test_userassessment1, item=self.test_item1, option=self.test_option1_1)
        TesteeResponse.objects.create(testeeassessment=self.test_userassessment1, item=self.test_item2, option=self.test_option2_2)
        current_status = self.test_userassessment1.status_update()
        self.assertEqual(current_status, 'passed')

    # def test_select_item_returns_item(self):
    #     """
    #     select_item() should return item 
    #     """    
    #     current_items = Item.objects.all().filter(itembank = self.test_userassessment1.assessment.itembank).filter(status='active')
    #     test_item = self.test_userassessment1.select_item(current_items)   
    #     self.assertContains(test_item, 'Test stem text')

# Finish writing tests for select_item()
