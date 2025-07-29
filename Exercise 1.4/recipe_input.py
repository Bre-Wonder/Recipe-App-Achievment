import pickle
import os

recipe_list = []
all_ingredients = []
n = int(input("How many recipes would you like to have? "))

# function that determines how difficult the recipe is


def calc_difficulty(recipe):
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        return 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        return 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        return 'Intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        return 'Hard'

# allows user to input a recipe of choice


def take_recipe():
    recipe_name = str(input("Please give the name of the recipe here: "))
    cooking_time = int(input("Please give the cooking time in minutes: "))
    ingredients = input(
        "Please list your ingredients here (please note to put a comma between each ingredient): ").split(', ')
    recipe = {'recipe_name': recipe_name, 'cooking_time': cooking_time,
              'ingredients': ingredients, }
    recipe['difficulty'] = calc_difficulty(recipe)
    return recipe


# for loop that loops over the take_recipe function the amount of times the user specifies and also review for
# ingredients that need to be added the all_ingredients list


for i in range(n):
    recipe = take_recipe()
    recipe_list.append(recipe)
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
            print(ingredient + ' added to your list')
        else:
            print(ingredient + ' is already on your list!')


data = {
    'recipe_list': recipe_list,
    'all_ingredients': all_ingredients
}

named_file = input(
    'What is the name of the file where you would like to store your recipes? ')
if not named_file.endswith('.bin'):
    named_file += '.bin'
    print('Your file name did not include .bin at the end. It has been added to your file name.')
else:
    print('Name convention done correctly')

redefine_file_path = os.path.join(os.getcwd(), named_file)


# opens binary file and gives the read command
try:
    recipe_details = open(redefine_file_path, 'rb')
    data = pickle.load(recipe_details)

# runs an error if file is not found in the correct file path or not found at all
except FileNotFoundError:
    print('File not found, please select another file')
    data = {
        'recipe_list': recipe_list,
        'all_ingredients': all_ingredients
    }

# runs an error when input is not the right type of value
except (pickle.UnpicklingError, EOFError):
    print('Error occurred while trying to read file')
    data = {
        'recipe_list': recipe_list,
        'all_ingredients': all_ingredients
    }

# closes file opened by pickle
else:
    recipe_details.close()
    print('Given_file closed for read only mode')

# abstracts values from data variable to split into two different lists
finally:
    recipe_list = data['recipe_list']
    all_ingredients = data['all_ingredients']
    all_ingredients.sort()

    with open(redefine_file_path, 'wb') as recipe_details:
        pickle.dump(data, recipe_details)
