from unittest import skip
from django.test import TestCase
from django.contrib.auth.models import User


from store.models import Category, Product


@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_exmaple(self):
        pass
