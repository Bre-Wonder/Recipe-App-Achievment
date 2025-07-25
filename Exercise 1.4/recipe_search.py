import pickle


def display_recipe(recipe):
    print('Recipe Information ---')
    print(f"Recipe: {recipe['recipe_name']}")
    print(f"Cooking Time (in minutes): {recipe['cooking_time']}")
    print(f"Ingredients: " + ', '.join(recipe['ingredients']))
    print(f"Difficulty Level: {recipe['difficulty']}")
