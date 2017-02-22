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