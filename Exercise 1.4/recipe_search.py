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

    try:
        index_number_chosen = int(input(
            'Please select number from index of ingredients: '))
        ingredient_searched = data['all_ingredients'][index_number_chosen]

    except ValueError:
        print('Value must be a number')

    except IndexError:
        print('That index number does not exist in you current index')

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


named_file_2 = input(
    'What is the name of the file where you would like to store the data for your recipes? ')
if not named_file_2.endswith('.bin'):
    named_file_2 += '.bin'
    print('Your file name did not include .bin at the end. It has been added to your file name.')
else:
    print('Name convention done correctly')

try:
    with open(named_file_2, 'rb') as recipe_lookup:
        data = pickle.load(recipe_lookup)


# runs an error if file is not found in the correct file path or not found at all
except FileNotFoundError:
    print('File not found, please select another file')

else:
    search_ingredients(data)
