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


for i in range(n):
    recipe = take_recipe(i)
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
            print(ingredient + ' added to your list')
        else:
            print(ingredient + ' is already on your list!')
    recipe_list.append(recipe)
