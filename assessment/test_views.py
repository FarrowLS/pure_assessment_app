from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

# ADD TEST CREATION HERE LATER

class AssessmentIndexTests(TestCase):
    def test_index_can_not_be_seen_by_anonymous_user(self):
        """
        The Assessment index page should be behind the login
        """
        response = self.client.get(reverse('assessmentindex'))
        self.assertEqual(response.status_code, 302)


    def test_index_exists(self):
        """
        The Assessment index page should be at /assessment
        """
        test_user_setup = User.objects.create_user(username='bob', password='secret')
        test_user = Client()
        test_user.login(username='bob', password='secret')  
        response = test_user.get(reverse('assessmentindex'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your tests")
