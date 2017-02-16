from django.test import TestCase


class FailingTest(TestCase):

    def test_failure(self):
        self.assertTrue(False)