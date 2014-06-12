from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from itembank.models import Itembank, Item, Option
from assessment.models import Assessment, TesteeAssessment, TesteeResponse

def create_itembank(name):
    """
    Creates an itembank with a name
    """
    return Itembank.objects.create(name=name)

def create_assessment(name, itembank):
    """
    Creates a test with a name and relationship to itembank
    """
    return Assessment.objects.create(name=name, itembank=itembank)

def create_item(itembank, stem_text):
    """
    Creates an item with stem text and relationship to an itembank
    """
    return Item.objects.create(itembank=itembank, stem_text=stem_text)

def create_option(item, option_text, correct_answer):
    """
    Creates an item with stem text and relationship to an itembank
    """
    return Option.objects.create(item=item, option_text=option_text, correct_answer=correct_answer) 

def create_testeeassessment(assessment, testee):
    """
    Creates a testee assessment with a relationship to an assessment and testee
    """
    return TesteeAssessment.objects.create(assessment=assessment, testee=testee)   

def create_testeeresponse(testeeassessment, item, option=None):
    """
    Creates a testee response with a relationship to a testee response, item and maybee and option
    """
    return TesteeResponse.objects.create(testeeassessment=testeeassessment, item=item, option=option)

class AssessmentIndexTests(TestCase):

    """"
    TO BE ADDED   
    def setUp(self):
       pass

    def tearDown(self):
       pass
    """

    def test_index_can_not_be_seen_by_anonymous_user(self):
        """
        The Assessment index page should be behind the login
        """
        response = self.client.get(reverse('assessmentindex'), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 302)

    def test_no_active_assesments(self):
        """
        The Assessment page should indicate there are no assessments to complete
        """
        test_user_setup = User.objects.create_user(username='bob', password='secret')
        test_user = Client()
        test_user.login(username='bob', password='secret')
        response = test_user.get(reverse('assessmentindex'), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You do not have any tests to complete at this time.")

    def test_active_assesments(self):
        """
        The assessment index page should have a list of active assessments, as links to the assessments, when they exist
        """
        test_itembank1 = create_itembank(name="Itembank1")
        test_assessment1 = create_assessment(name="Test1", itembank=test_itembank1)
        test_user_setup = User.objects.create_user(username='bob', password='secret')
        test_user = Client()
        test_userassessment1 = create_testeeassessment(test_assessment1, test_user_setup) 
        test_user.login(username='bob', password='secret')  
        response = test_user.get(reverse('assessmentindex'), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test1")
        self.assertContains(response, '<a href="/assessments/1/">') # Checks links to assessments

    def test_no_active_assesments_from_other_user(self):
        """
        The assessment index page should not have active assessments from other users
        """
        test_itembank1 = create_itembank(name="Itembank1")
        test_assessment1 = create_assessment(name="Test1", itembank=test_itembank1)
        test_user_setup = User.objects.create_user(username='bob', password='secret')
        test_userassessment1 = create_testeeassessment(test_assessment1, test_user_setup)
        test_user_setup2 = User.objects.create_user(username='joe', password='secret')
        test_user = Client()
        test_user.login(username='joe', password='secret')
        response = test_user.get(reverse('assessmentindex'), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Test1")

    def test_no_completed_assesments(self):
        """
        The Assessment page should indicate there are no completed assessments
        """
        test_user_setup = User.objects.create_user(username='bob', password='secret')
        test_user = Client()
        test_user.login(username='bob', password='secret')
        response = test_user.get(reverse('assessmentindex'), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You have not completed any tests yet.")

    # TO BE ADDED def test_completed_assesments(self): 

    # TO BE ADDED def test_item_display(self):

    # TO BE ADDED def test_no_completed_assesments_from_other_user(self):

class AssessmentItemTests(TestCase):
    def test_assessment_item_can_not_be_seen_by_anonymous_user(self):
        """
        An assessment item page should be behind the login
        """
        test_itembank1 = create_itembank(name="Itembank1")
        test_assessment1 = create_assessment(name="Test1", itembank=test_itembank1)
        test_user_setup = User.objects.create_user(username='bob', password='secret')
        test_userassessment1 = create_testeeassessment(test_assessment1, test_user_setup)
        response = self.client.get(reverse('assessmentitem', args=(test_userassessment1.id,)), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 302)

    def test_assessment_item_can_not_be_seen_by_user_who_is_not_the_testee(self):
        """
        The assessment item should not be able to be seen by a user who is not the testee
        """
        test_itembank1 = create_itembank(name="Itembank1")
        test_assessment1 = create_assessment(name="Test1", itembank=test_itembank1)
        test_user_setup = User.objects.create_user(username='bob', password='secret')
        test_userassessment1 = create_testeeassessment(test_assessment1, test_user_setup)
        test_user_setup2 = User.objects.create_user(username='joe', password='secret')
        test_user = Client()
        test_user.login(username='joe', password='secret')
        response = test_user.get(reverse('assessmentitem', args=(test_userassessment1.id,)), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 403) 

    def test_assessment_item_can_be_seen_by_testee(self):
        """
        An assessment item page should be seen by testee
        """
        test_itembank1 = create_itembank(name="Itembank1")
        test_assessment1 = create_assessment(name="Test1", itembank=test_itembank1)
        test_item1 = create_item(itembank=test_itembank1, stem_text="Test stem text1")
        test_option1 = create_option(item=test_item1, option_text="True", correct_answer=True)
        test_option2 = create_option(item=test_item1, option_text="False", correct_answer=False) 
        test_user_setup = User.objects.create_user(username='bob', password='secret')
        test_userassessment1 = create_testeeassessment(test_assessment1, test_user_setup)
        test_user = Client()
        test_user.login(username='bob', password='secret')
        response = test_user.get(reverse('assessmentitem', args=(test_userassessment1.id,)), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test stem text1")

    def test_assessment_unanswered_item_will_be_served(self):
        """
        Unanswered items should be served until answered
        """
        test_itembank1 = create_itembank(name="Itembank1")
        test_assessment1 = create_assessment(name="Test1", itembank=test_itembank1)
        test_item1 = create_item(itembank=test_itembank1, stem_text="Test stem text1")
        test_option1_1 = create_option(item=test_item1, option_text="True", correct_answer=True)
        test_option1_2 = create_option(item=test_item1, option_text="False", correct_answer=False)
        test_item2 = create_item(itembank=test_itembank1, stem_text="Test stem text2")
        test_option2_1 = create_option(item=test_item2, option_text="True", correct_answer=True)
        test_option2_2 = create_option(item=test_item2, option_text="False", correct_answer=False)
        test_user_setup = User.objects.create_user(username='bob', password='secret')
        test_userassessment1 = create_testeeassessment(test_assessment1, test_user_setup)

        # test_testeeresponse = create_testeeresponse(test_userassessment1, test_item2, test_option2_1) # for a test

        test_testeeresponse = create_testeeresponse(test_userassessment1, test_item1)
        test_user = Client()
        test_user.login(username='bob', password='secret')
        response = test_user.get(reverse('assessmentitem', args=(test_userassessment1.id,)), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test stem text1")

    def test_assessment_answered_item_should_not_be_served(self):
        """
        Answered items should not be served
        """
        """

        TEST TO BE FIXED
        
        test_itembank1 = create_itembank(name="Itembank1")
        test_assessment1 = create_assessment(name="Test1", itembank=test_itembank1)
        test_item1 = create_item(itembank=test_itembank1, stem_text="Test stem text1")
        test_option1_1 = create_option(item=test_item1, option_text="True", correct_answer=True)
        test_option1_2 = create_option(item=test_item1, option_text="False", correct_answer=False)
        test_item2 = create_item(itembank=test_itembank1, stem_text="Test stem text2")
        test_option2_1 = create_option(item=test_item2, option_text="True", correct_answer=True)
        test_option2_2 = create_option(item=test_item2, option_text="False", correct_answer=False)
        test_user_setup = User.objects.create_user(username='bob', password='secret')
        test_userassessment1 = create_testeeassessment(test_assessment1, test_user_setup)
        # test_testeeresponse = create_testeeresponse(test_userassessment1, test_item1, test_option1_1)
        test_user = Client()
        test_user.login(username='bob', password='secret')
        test_testeeresponse = create_testeeresponse(test_userassessment1, test_item1, test_option1_1)
        response = test_user.get(reverse('assessmentitem', args=(test_userassessment1.id,)), **{'wsgi.url_scheme': 'https'})
        # TO BE UPDATED - CHANGE BACK TO 200 AFTER ITEM SELECTION IS UPDATED
        # self.assertEqual(response.status_code, 302) 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "text")
        """

    # Test to show passing assessment

    # Test to show failing assessment

    # Not enough items to give assessment
