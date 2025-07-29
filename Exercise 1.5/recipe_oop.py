class Recipe(object):
    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        # self.ingredients = ingredients[] make ingredients into a list
        self.cooking_time = cooking_time
        self.difficulty = self.calculate_difficulty()

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
