from sqlalchemy.types import Integer, String
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# function that allows user to connect to the database and sets it equal to a variable
engine = create_engine("mysql://cf-python:password@localhost/my_database")

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# defining recipe class which inherits traits from define Base


class Recipe(Base):

    # creating a table (definig the structure)
    __tablename__ = 'final_recipes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # quick read for recipe info
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + "Difficulty Level: " + str(self.difficulty) + ">"

    # puts recipe data into a string format for the user
    def __str__(self):
        return (
            "Recipe Information *5\n"
            f"ID: {self.id} | Recipe: {self.name}\n"
            f"Cooking Time (in minutes): {self.cooking_time}\n"
            f"Ingredients:  {', '.join(self.return_ingredients_as_list())}\n"
            f"Difficulty Level: {self.difficulty}"
        )

    # calculates the difficulty of each recipe based on cooking time and number of ingredients
    def calculate_difficulty(self, cooking_time, ingredients):
        if cooking_time < 10 and len(ingredients) < 4:
            self.difficulty = 'Easy'
        elif cooking_time < 10 and len(ingredients) >= 4:
            self.difficulty = 'Medium'
        elif cooking_time >= 10 and len(ingredients) < 4:
            self.difficulty = 'Intermediate'
        elif cooking_time >= 10 and len(ingredients) >= 4:
            self.difficulty = 'Hard'
        return self.difficulty

    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        else:
            ingredients_list = [ingredient.strip()
                                for ingredient in self.ingredients.split(', ')]
            return ingredients_list


Base.metadata.create_all(engine)

# allows user to create and add a recipe


def create_recipe():
    while True:
        recipe_name = str(input("Please give the name of the recipe here: "))
        if len(recipe_name) > 50:
            print('Name you have selected is not under 50 characters.')
        elif not recipe_name.isalpha():
            print('Recipe name must only contain letters')
        else:
            break

    while True:
        cooking_time = input("Please give the cooking time in minutes: ")
        if not cooking_time.isnumeric():
            print(
                'Your input must be a number. Please select a number to respresnet time in minutes')
        else:
            break

    ingredients = []
    num_of_ingredients = int(
        input('How many ingredients does your recipe have?'))

    for i in range(num_of_ingredients):
        ing = input(f'Please give ingredient number {i + 1}: ')
        ingredients.append(ing)

    ingredients_stringed = ', '.join(ingredients)

    # creates a Recipe object
    recipe_entry = Recipe(
        name=recipe_name,
        ingredients=ingredients_stringed,
        cooking_time=cooking_time
    )

    recipe_entry.calculate_difficulty(recipe_entry.cooking_time, ingredients)

    # adding and commiting change to database
    session.add(recipe_entry)
    session.commit()
