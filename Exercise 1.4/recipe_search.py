import pickle


def display_recipe(recipe):
    print('Recipe Information ---')
    print(f"Recipe: {recipe['recipe_name']}")
    print(f"Cooking Time (in minutes): {recipe['cooking_time']}")
    print(f"Ingredients: " + ', '.join(recipe['ingredients']))
    print(f"Difficulty Level: {recipe['difficulty']}")


def search_ingredients(data):
    print('All Ingredients ---')
    for index, ingredient in enumerate(data['all_ingredients']):
        print(f"{index}: {ingredient}")


named_file_2 = input(
    'What is the name of the file where you would like to store the data for your recipes? ')
if not named_file_2.endswith('.bin'):
    named_file_2 += '.bin'
    print('Your file name did not include .bin at the end. It has been added to your file name.')
else:
    print('Name convention done correctly')
