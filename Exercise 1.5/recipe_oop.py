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
