recipe_list = []
ingredients_list = []

n = int(input("How many recipes would you like to have? "))


def take_recipe():
    name = str(input("Please give the name of the recipe here: "))
    cooking_time = int(input("Please give the cooking time in minutes: "))
    ingredients = input(
        "Please list your ingredients here (please note to put a comma between each ingredient): ").split(', ')
    recipe = {'name': name, 'cooking_time': cooking_time,
              'ingredients': ingredients}
    print(recipe)


take_recipe()
