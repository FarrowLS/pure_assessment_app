from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from about.models import Page

class AboutIndexTests(TestCase):

    def setUp(self):
        Page.objects.create(title="Test1 Title", body="Test1 body.")
        Page.objects.create(title="Test2 Title", body="Test2 body.")

    def tearDown(self):
        pass   

    def test_index_exists(self):
        """
        The About index page should be at /about
        """
        response = self.client.get(reverse('aboutindex'), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)

    def test_index_has_readme_text(self):
        """
        The About index page should be pulling in text from the README file 
        """
        response = self.client.get(reverse('aboutindex'), **{'wsgi.url_scheme': 'https'})
        self.assertContains(response, "Django")

    def test_index_has_list_of_about_pages(self):
        """
        The About index page should show a list of About pages
        """
        response = self.client.get(reverse('aboutindex'), **{'wsgi.url_scheme': 'https'})
        self.assertQuerysetEqual(
            response.context['text2'],
             ['<Page: Test1 Title>', '<Page: Test2 Title>']
        )


class AboutDetailTests(TestCase):

    def setUp(self):
        self.test_page = Page.objects.create(title="Test Title", body="This is a test body.") # create_page(title="Test Title", body="This is a test body.")

    def tearDown(self):
       pass   

    def test_detail_page_is_accessable(self):
        """
        An About detail page should be accessable to an anonymous user
        """
        response = self.client.get(reverse('aboutdetail', args=(self.test_page.id,)), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)

    def test_detail_page_has_text(self):
        """
        An About detail page should have title and body text on it
        """
        response = self.client.get(reverse('aboutdetail', args=(self.test_page.id,)), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Title")
        self.assertContains(response, "This is a test body.")

