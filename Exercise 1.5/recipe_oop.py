class Recipe(object):
    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        # self.ingredients = ingredients[] make ingredients into a list
        self.cooking_time = cooking_time
        self.difficulty = self.calculate_difficulty()

    def __str__(self):
        output = str('Recipe Information ---\n')
        + str('Name: ') + str(self.name)
        + '\n' + str('Ingredients: ') + str(self.ingredients)
        + '\n' + str('Cooking Time in minutes: ') + str(self.cooking_time)
        + '\n' + str('Difficulty: ') + str(self.difficulty)
        return output

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def add_ingredients(self, ingredients_length):

        update_all_ingredients()

    def calculate_difficulty(self, cooking_time, ingredients, difficulty):
        if cooking_time < 10 and len(ingredients) < 4:
            return 'Easy'
        elif cooking_time < 10 and len(ingredients) >= 4:
            return 'Medium'
        elif cooking_time >= 10 and len(ingredients) < 4:
            return 'Intermediate'
        elif cooking_time >= 10 and len(ingredients) >= 4:
            return 'Hard'


tea = Recipe('Tea', ['Tea Leaves', 'Sugar', 'Water'], 5)
coffee = Recipe('Coffee', ['Coffee Powder', 'Sugar', 'Water'], 5)
cake = Recipe('Cake', ['Sugar', 'Butter', 'Eggs',
              'Vanilla Essence', 'Flour', 'Baking Powder', 'Milk'], 50)
banana_smoothie = Recipe('Banana Smoothie', [
                         'Bananas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice Cubes'], 5)
