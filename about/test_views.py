from django.core.urlresolvers import reverse
from django.test import TestCase

from about.models import Page

def create_page(title, body):
    """
    Creates a pages with a title and body
    """
    return Page.objects.create(title=title, body=body)

class AboutIndexTests(TestCase):
    def test_index_has_readme_text(self):
        """
        The About index page should be pulling in text from the README file 
        """
        response = self.client.get(reverse('aboutindex'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django")

class AboutDetailTests(TestCase):
    def test_detail_page_has_text(self):
        """
        An About detail page should have title and body text on it
        """
        test_page = create_page(title="Test Title", body="This is a test body.")
        # response = self.client.get(reverse('aboutdetail'))
        response = self.client.get(reverse('aboutdetail', args=(test_page.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Title")
        self.assertContains(response, "This is a test body.")

