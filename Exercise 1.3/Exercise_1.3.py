recipe_list = []
ingredients_list = []

n = int(input("How many recipes would you like to have? "))

# function that takes the action of collecting a recipe from user


def take_recipe():
    recipe_name = str(input("Please give the name of the recipe here: "))
    cooking_time = int(input("Please give the cooking time in minutes: "))
    ingredients = input(
        "Please list your ingredients here (please note to put a comma between each ingredient): ").split(', ')
    recipe = {'recipe_name': recipe_name, 'cooking_time': cooking_time,
              'ingredients': ingredients}
    return recipe

# for loop that added ingredients to the list that have not already been added


for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
            print(ingredient + ' added to your list')
        else:
            print(ingredient + ' is already on your list!')
    recipe_list.append(recipe)

    # decifering if a given recipe is difficult or not

    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        difficulty = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        difficulty = 'Intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'Hard'
    recipe['difficulty'] = difficulty

    for recipe in recipe_list:
        print(f'Recipe: {recipe['recipe_name']}')
        print(f'Cooking Time (in minutes): {recipe['cooking_time']}')
        print(f'Ingredients: ' + ', '.join(recipe['ingredients']))
        print(f'Difficulty Level: {recipe['difficulty']}')
