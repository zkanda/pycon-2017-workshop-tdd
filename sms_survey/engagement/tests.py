from unittest.mock import patch
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from .views import index


class HomePageTest(TestCase):

    def test_index_return_correct_html(self):
        response = self.client.get("/")
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Surveyor</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'index.html')


class SendSMSPageTest(TestCase):

    def test_sms_page_return_correct_html(self):
        response = self.client.get("/send_sms/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'send_sms.html')

    @patch('requests.post')
    def test_when_send_an_sms_redirect_to_homepage(self, mock_post):
        # Redirect to home page
        response = self.client.post("/send_sms/", {"contact": "093487392", "message": "What is your name?"})

        self.assertEqual(response.status_code, 302)

    @patch('requests.post')
    def test_chikka_api_is_called(self, mock_post):
        # chikka api is being called
        
        # post
        response = self.client.post("/send_sms/", {"contact": "093487392", "message": "What is your name?"})

        # send chikka
        mock_post.assert_called()
