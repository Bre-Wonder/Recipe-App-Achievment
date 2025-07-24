import pickle

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
