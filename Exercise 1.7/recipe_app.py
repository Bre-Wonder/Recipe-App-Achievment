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
    # input for name of the recipe
    while True:
        recipe_name = str(input("Please give the name of the recipe here: "))
        if len(recipe_name) > 50:
            print('Name you have selected is not under 50 characters.')
        elif not recipe_name.isalpha():
            print('Recipe name must only contain letters')
        else:
            break

    # input for cooking time
    while True:
        cooking_time = input("Please give the cooking time in minutes: ")
        if not cooking_time.isnumeric():
            print(
                'Your input must be a number. Please select a number to respresnet time in minutes')
        else:
            break

    # input for ingredients
    ingredients = []
    num_of_ingredients = int(
        input('How many ingredients does your recipe have?'))

    for i in range(num_of_ingredients):
        ing = input(f'Please give ingredient number {i + 1}: ')
        ingredients.append(ing)

    # makes ingredient list into a string
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

# a user selects a recipe to delete and deletes if from the table and the database


def delete_recipe():
    # query to find all recipes in the database
    all_recipes = session.query(Recipe).all()

    # looking to see if there are recipes in the database table, otherwise sends user back to main menu
    if len(all_recipes) <= 0:
        return main_menu()

    # gives us a list of all recipes which they can delete
    recipe_ids = []

    print('Here are you recipes already created: ')
    for row in all_recipes:
        print('ID: ', row.id)
        print('Name: ', row.name)
        recipe_ids.append(row.id)

    # user input for which recipe they would like to delete by id
    try:
        user_selected_id = int(input(
            'Please enter the ID of the recipe that you would like to delete:'))

    # checks for value to be a number
    except ValueError:
        print('Invalid input. Please enter a number')
        return

    # checks to see if id matches one in the database, otherwiese throws an error
    if user_selected_id not in recipe_ids:
        print('That recipe id does not exist')
        return main_menu()

    recipe_to_be_deleted = session.query(Recipe).filter(
        Recipe.id == user_selected_id).one()

    # confirms with user that this is the recipe they would like to delete
    user_confirmation = input(
        f'Are you sure you would like to delete your {recipe_to_be_deleted.name} recipe? Please type "yes" or "no".')
    if user_confirmation == 'no':
        print('Recipe get. Returning you to main menu')
        return main_menu()
    elif user_confirmation == 'yes':
        # deletes recipe from table and database
        session.delete(recipe_to_be_deleted)
        # commits changes
        session.commit()
        print('Your recipe has been successfully deleted')

    else:
        print('Error: Invalid entry. Please type yes or no')


# this hold the main menu that the user sees when they first start up the application
def main_menu():
    choice = ''
    while (choice != 'quit'):
        print('MAIN MENU')
        print('----------------------')
        print('----------------------')
        print('What would you like to do? Pick a number that corresponds with the option you would like to select')
        print('1. Create a new recipe')
        print('2. View all your recipes')
        print('3. Search for a recipe by an ingredient')
        print('4. Edit a recipe')
        print('5. Delete a recipe')
        print("Type 'quit' to exit the program")
        choice = input('Your Choice: ')

        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingrediets()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == 'quit':
            print('You selected quit. Program has stopped.')
            session.close()
            engine.dispose()
        else:
            print('Selection not valid. Please select a number between 1-5 or "quit".')


main_menu()
