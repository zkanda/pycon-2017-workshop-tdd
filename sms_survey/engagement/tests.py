from unittest.mock import patch
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from .views import index
from .models import Messages


class HomePageTest(TestCase):

    def test_index_return_correct_html(self):
        response = self.client.get("/")
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Surveyor</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'index.html')
    

    def test_should_return_content_data(self):
        Messages.objects.create(
            id=1,
            mobile_number="9847543895",
            message="This is a message",
        )
        response = self.client.get("/")
        html = response.content.decode('utf8')
        self.assertIn("This is a message", html)


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

class MessageModelTest(TestCase):
    
    def setUp(self):
        Messages.objects.create(
            id=1,
            mobile_number="9847543895",
            message="This is a message",
        )

    def test_can_save_data(self):
        # We can save data
        m = Messages.objects.all()
        self.assertTrue(len(m) > 0)

    def test_can_retreive_data(self):
        # Retreive data
        m = Messages.objects.get(pk=1)
        self.assertEqual(m.mobile_number, "9847543895")

class ChikkaReceiverTest(TestCase):

    def test_should_return_200(self):
        # it should return 200
        response = self.client.post("/chikka_receiver/", data={
            "mobile_number": "0945983495439",
            "message": "Elpedio Adoptante"
        })
        self.assertEqual(response.status_code, 200)

    def test_it_should_save_to_database(self):
        # it should save to database
        self.client.post("/chikka_receiver/", data={
            "mobile_number": "0945983495439",
            "message": "Elpedio Adoptante"
        })
        m = Messages.objects.all()
        self.assertTrue(len(m) > 0)
        self.assertEqual(m[0].mobile_number, '0945983495439')
