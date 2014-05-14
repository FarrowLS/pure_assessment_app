from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from about.models import Page

def create_page(title, body):
    """
    Creates a pages with a title and body
    """
    return Page.objects.create(title=title, body=body)

class AboutIndexTests(TestCase):
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
        test_page1 = create_page(title="Test1 Title", body="Test1 body.")
        test_page2 = create_page(title="Test2 Title", body="Test2 body.")

        response = self.client.get(reverse('aboutindex'), **{'wsgi.url_scheme': 'https'})
        self.assertQuerysetEqual(
            response.context['text2'],
             ['<Page: Test1 Title>', '<Page: Test2 Title>']
        )


class AboutDetailTests(TestCase):
    def test_detail_page_not_accessable(self):
        """
        An About detail page should be accessable to an anonymous user
        """
        test_page = create_page(title="Secret Title", body="This is a secret body.") 
        response = self.client.get(reverse('aboutdetail', args=(test_page.id,)), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)

    def test_detail_page_has_text(self):
        """
        An About detail page should have title and body text on it
        """
        test_page = create_page(title="Test Title", body="This is a test body.")
        test_user_setup = User.objects.create_user(username='bob', password='secret')
        test_user = Client()
        test_user.login(username='bob', password='secret')
        # Don't think I need this # response = self.client.get(reverse('aboutdetail'))
        # response = self.client.get(reverse('aboutdetail', args=(test_page.id,)))
        response = test_user.get(reverse('aboutdetail', args=(test_page.id,)), **{'wsgi.url_scheme': 'https'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Title")
        self.assertContains(response, "This is a test body.")

