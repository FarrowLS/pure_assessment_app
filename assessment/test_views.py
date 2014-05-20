from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from itembank.models import Itembank
from assessment.models import Assessment

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

class AssessmentIndexTests(TestCase):
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
        The assessment index page should have a list of active assessments when they exist
        """
        test_itembank1 = create_itembank(name="Itembank1")
        test_assessment1 = create_assessment(name="Test1", itembank=test_itembank1)
        test_user_setup = User.objects.create_user(username='bob', password='secret')
        test_user = Client()
        test_user.login(username='bob', password='secret')  
        response = test_user.get(reverse('assessmentindex'), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test1")

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

 
