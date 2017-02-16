from django.core.urlresolvers import resolve
from django.test import TestCase
from .views import index


class HomePageTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, index)