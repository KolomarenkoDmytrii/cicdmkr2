from django.test import TestCase

# Create your tests here.

from django.test import RequestFactory, TestCase
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.test.client import Client

from .models import Category, Recipe
import recipe.views


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()
        self.recipes = [
            Recipe.objects.create(
                title="food 0",
                description="desc 0",
                instructions="top_secret 0",
                ingredients="top_secret ingr 0",
                category=Category.objects.create(name='Catca')
            ),
            Recipe.objects.create(
                title="food 1",
                description="desc 1",
                instructions="top_secret 1",
                ingredients="top_secret ingr 1",
                category=Category.objects.create(name='Nurco')
            ),
            Recipe.objects.create(
                title="food 3",
                description="desc 3",
                instructions="top_secret 3",
                ingredients="top_secret ingr 3",
                category=Category.objects.create(name='Merca')
            ),
        ]

    def test_main_view(self):
        # Create an instance of a GET request.
        # request = self.factory.get(reverse('main'))
        request = self.client.get(reverse('main'))

        # Test my_view() as if it were deployed at /customer/details
        response = recipe.views.main(request)
        self.assertEqual(response.status_code, 200)
        # # # # self.assertAlmostEqual(set(response.context['recipes']), set(self.recipes))
