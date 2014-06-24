from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from itembank.models import Itembank, Item, Option
from assessment.models import Assessment, TesteeAssessment, TesteeResponse

class AssessmentIndexAnonymousTests(TestCase):
   
    def setUp(self):
       pass

    def tearDown(self):
       pass

    def test_index_can_not_be_seen_by_anonymous_user(self):
        """
        The Assessment index page should be behind the login
        """
        response = self.client.get(reverse('assessmentindex'), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 302)


class AssessmentIndexAuthenticatedTests(TestCase):
   
    def setUp(self):
        self.test_user1_setup = User.objects.create_user(username='bob', password='secret')
        # self.test_user = Client()
        # self.test_user.login(username='bob', password='secret')
        self.test_user2_setup = User.objects.create_user(username='fred', password='secret')
        self.test_itembank1 = Itembank.objects.create(name="Itembank1")
        self.test_assessment1 = Assessment.objects.create(name="Test1", itembank=self.test_itembank1)
        
    def tearDown(self):
        self.test_user1_setup.delete()
        # self.test_user.delete()
        self.test_user2_setup.delete()  
        self.test_itembank1.delete()  
        self.test_assessment1.delete()

    def test_no_active_assesments(self):
        """
        The Assessment page should indicate there are no assessments to complete
        """
        self.test_user = Client()
        self.test_user.login(username='bob', password='secret')
        response = self.test_user.get(reverse('assessmentindex'), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You do not have any tests to complete at this time.")

    def test_active_assesments(self):
        """
        The assessment index page should have a list of active assessments, as links to the assessments, when they exist
        """
        test_userassessment1 = TesteeAssessment.objects.create(assessment=self.test_assessment1, testee=self.test_user1_setup) 
        self.test_user = Client()
        self.test_user.login(username='bob', password='secret')  
        response = self.test_user.get(reverse('assessmentindex'), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test1")
        self.assertContains(response, '<a href="/assessments/%d/">' % test_userassessment1.id) # Checks links to assessments

    def test_no_active_assesments_from_other_user(self):
        """
        The assessment index page should not have active assessments from other users
        """
        test_userassessment2 = TesteeAssessment.objects.create(assessment=self.test_assessment1, testee=self.test_user2_setup)
        self.test_user = Client()
        self.test_user.login(username='bob', password='secret')
        response = self.test_user.get(reverse('assessmentindex'), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)  
        self.assertNotContains(response, "Test1")

    def test_no_completed_assesments(self):
        """
        The Assessment page should indicate there are no completed assessments
        """

        self.test_user = Client()
        self.test_user.login(username='bob', password='secret')
        response = self.test_user.get(reverse('assessmentindex'), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You have not completed any tests yet.")

    # TO BE ADDED def test_completed_assesments(self): 

    # TO BE ADDED def test_item_display(self):

    # TO BE ADDED def test_no_completed_assesments_from_other_user(self):

class AssessmentItemTests(TestCase):

    def setUp(self):
        # Setup for itembanks and assessments
        self.test_itembank1 = Itembank.objects.create(name="Itembank1")
        self.test_assessment1 = Assessment.objects.create(name="Test1", itembank=self.test_itembank1)
        # Setup for items and their options
        self.test_item1 = Item.objects.create(itembank=self.test_itembank1, stem_text="Test stem text1")
        self.test_option1_1 = Option.objects.create(item=self.test_item1, option_text="True", correct_answer=True)
        self.test_option1_2 = Option.objects.create(item=self.test_item1, option_text="False", correct_answer=False)
        self.test_item2 = Item.objects.create(itembank=self.test_itembank1, stem_text="Test stem text2")
        self.test_option2_1 =  Option.objects.create(item=self.test_item2, option_text="True", correct_answer=True)
        self.test_option2_2 = Option.objects.create(item=self.test_item2, option_text="False", correct_answer=False)

        # self.test_item3 = Item.objects.create(itembank=self.test_itembank1, stem_text="Test stem text3")
        # self.test_option3_1 =  Option.objects.create(item=self.test_item3, option_text="True", correct_answer=True)
        # self.test_option3_2 = Option.objects.create(item=self.test_item3, option_text="False", correct_answer=False)

        # Setup for users and user assessments
        self.test_user_setup1 = User.objects.create_user(username='bob', password='secret')
        self.test_user_setup2 = User.objects.create_user(username='joe', password='secret')
        self.test_userassessment1 = TesteeAssessment.objects.create(assessment=self.test_assessment1, testee=self.test_user_setup1)

    def tearDown(self):
       pass

    def test_assessment_item_can_not_be_seen_by_anonymous_user(self):
        """
        An assessment item page should be behind the login
        """
        response = self.client.get(reverse('assessmentitem', args=(self.test_userassessment1.id,)), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 302)

    def test_assessment_item_can_not_be_seen_by_user_who_is_not_the_testee(self):
        """
        The assessment item should not be able to be seen by a user who is not the testee
        """
        test_user = Client()
        test_user.login(username='joe', password='secret')
        response = test_user.get(reverse('assessmentitem', args=(self.test_userassessment1.id,)), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 403) 

    def test_assessment_item_can_be_seen_by_testee(self):
        """
        An assessment item page should be seen by testee
        """
        test_user = Client()
        test_user.login(username='bob', password='secret')
        response = test_user.get(reverse('assessmentitem', args=(self.test_userassessment1.id,)), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test stem text")

    def test_assessment_unanswered_item_will_be_served(self):
        """
        Unanswered items should be served until answered
        """
        test_testeeresponse = TesteeResponse.objects.create(testeeassessment=self.test_userassessment1, item=self.test_item1) # create_testeeresponse(self.test_userassessment1, self.test_item1)
        test_user = Client()
        test_user.login(username='bob', password='secret')
        response = test_user.get(reverse('assessmentitem', args=(self.test_userassessment1.id,)), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test stem text1")

    # def test_assessment_answered_item_should_not_be_served(self):
        """
        Answered items should not be served
        """
        # TEST TO BE FIXED 

        # test_user = Client()
        # test_user.login(username='bob', password='secret')

        # test_testeeresponse = TesteeResponse.objects.create(testeeassessment=self.test_userassessment1, item=self.test_item2) # , option=self.test_option2_1)

        # response = test_user.get(reverse('assessmentitem', args=(self.test_userassessment1.id,)), **{'wsgi.url_scheme': 'https'})
        
        # TO BE UPDATED - CHANGE BACK TO 200 AFTER ITEM SELECTION IS UPDATED
        # self.assertEqual(response.status_code, 302) 

        # self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "text2")
        

    # Test to show passing assessment

    # Test to show failing assessment

    # Not enough items to give assessment
