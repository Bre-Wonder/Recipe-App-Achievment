import pickle
import os


def display_recipe(recipe):
    print('Recipe Information ---')
    print(f"Recipe: {recipe['recipe_name']}")
    print(f"Cooking Time (in minutes): {recipe['cooking_time']}")
    print(f"Ingredients: " + ', '.join(recipe['ingredients']))
    print(f"Difficulty Level: {recipe['difficulty']}")


def search_ingredients(data):
    print('All Ingredients ---')
    # adds index number to each ingredient in the list
    for index, ingredient in enumerate(data['all_ingredients']):
        print(f"{index}: {ingredient}")

    # allows user to pick out an ingredient based on its index number
    try:
        index_number_chosen = int(input(
            'Please select number from index of ingredients: '))
        ingredient_searched = data['all_ingredients'][index_number_chosen]

    except ValueError:
        print('Value must be a number')

    except IndexError:
        print('That index number does not exist in you current index')

    # if no errors are found, gives a list of recipes that have the selected ingredient in it
    else:
        matching_recipe = []
        for recipe in data['recipe_list']:
            if ingredient_searched in recipe['ingredients']:
                matching_recipe.append(recipe['recipe_name'])

        if matching_recipe:
            for name in matching_recipe:
                print(name)
        else:
            print('No recipes contain this ingredient')


# allows user to slect name for .bin file
named_file_2 = input(
    'What is the name of the file where you would like to store the data for your recipes? ')
if not named_file_2.endswith('.bin'):
    named_file_2 += '.bin'
    print('Your file name did not include .bin at the end. It has been added to your file name.')
else:
    print('Name convention done correctly')

# opens file and sets data equal to the loaded file
try:
    with open(named_file_2, 'rb') as recipe_lookup:
        data = pickle.load(recipe_lookup)


# runs an error if file is not found in the correct file path or not found at all
except FileNotFoundError:
    print('File not found, please select another file')

# executes function
else:
    search_ingredients(data)
    print('Success')
