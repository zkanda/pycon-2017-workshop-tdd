from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from .views import index


class HomePageTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, index)

    def test_index_return_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Surveyor</title>', html)
        self.assertTrue(html.endswith('</html>'))