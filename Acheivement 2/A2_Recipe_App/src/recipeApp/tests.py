from django.test import TestCase
from .models import Recipe
# to access Recipe model
from django.db import models

# Create your tests here.


class RecipeModelTest(TestCase):

    def setUpTestData():
        Recipe.objects.create(name='Spaghetti', ingredients='Meatballs, Noodles, Tomato Sauce',
                              cooking_time=25, description='Gather around with your family for warm fall meal. The tomatoes are flavorful and the noodles hit the spot. Join in and enjoy this recipe.')

    def test_recipe_name(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_ingredients_length(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'ingredients' field and use it to query its max_length
        max_length = recipe._meta.get_field('ingredients').max_length

        # Compare the value to the expected result i.e. 255
        self.assertEqual(max_length, 255)

    def test_cooking_time_type(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'cooking_time' field and use it to query if its an integer
        field = recipe._meta.get_field('cooking_time')

        # checkes if cooking_time is an integer
        self.assertIsInstance(field, models.IntegerField)

    def test_recipe_description(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'description' field and use it to query its data
        field_label = recipe._meta.get_field('description').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'description')
