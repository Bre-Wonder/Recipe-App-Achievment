import pickle

# allows user to input a recipe of choice


def take_recipe():
    recipe_name = str(input("Please give the name of the recipe here: "))
    cooking_time = int(input("Please give the cooking time in minutes: "))
    ingredients = input(
        "Please list your ingredients here (please note to put a comma between each ingredient): ").split(', ')
    difficulty = calc_difficulty()
    recipe = {'recipe_name': recipe_name, 'cooking_time': cooking_time,
              'ingredients': ingredients, 'difficulty': difficulty}
    return recipe

# function that determines how difficult the recipe is


def calc_difficulty():
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        difficulty = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        difficulty = 'Intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'Hard'
    recipe['difficulty'] = difficulty
