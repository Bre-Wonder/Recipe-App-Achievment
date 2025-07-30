class Recipe(object):

    all_ingredients = []

    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = self.calculate_difficulty()

    def __str__(self):
        output = (
            'Recipe Information ---\n'
            + 'Name: ' + str(self.name)
            + '\nIngredients: ' + str(self.ingredients)
            + '\nCooking Time in minutes: ' + str(self.cooking_time)
            + '\nDifficulty: ' + self.difficulty
        )
        return output

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def add_ingredients(self, ingredients):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)
            self.update_all_ingredients()

    def get_ingredients(self):
        return self.ingredients

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            return 'Easy'
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            return 'Medium'
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            return 'Intermediate'
        elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
            return 'Hard'

    def get_difficulty(self):
        self.difficulty = self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredients):
        if ingredients in self.ingredients:
            return True
        else:
            return False

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)


def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)


tea = Recipe('Tea', ['Tea Leaves', 'Sugar', 'Water'], 5)
coffee = Recipe('Coffee', ['Coffee Powder', 'Sugar', 'Water'], 5)
cake = Recipe('Cake', ['Sugar', 'Butter', 'Eggs',
              'Vanilla Essence', 'Flour', 'Baking Powder', 'Milk'], 50)
banana_smoothie = Recipe('Banana Smoothie', [
                         'Bananas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice Cubes'], 5)

recipe_list = [tea, coffee, cake, banana_smoothie]

print(recipe_search('Water'))
print(recipe_search('Sugar'))
print(recipe_search('Bananas'))
