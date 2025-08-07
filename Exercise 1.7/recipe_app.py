from sqlalchemy.types import Integer, String
from sqlalchemy import Column
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
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
        return f"<Recipe ID: {self.id} - {self.name} | Difficulty Level: {self.difficulty}>"

    # puts recipe data into a string format for the user
    def __str__(self):
        return (
            "Recipe Information ---\n"
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
        input('How many ingredients does your recipe have? '))

    for i in range(num_of_ingredients):
        ing = input(f'Please give ingredient number {i + 1}: ')
        ingredients.append(ing)

    # makes ingredient list into a string
    ingredients_stringed = ', '.join(ingredients)

    # creates a Recipe object
    recipe_entry = Recipe(
        name=recipe_name,
        ingredients=ingredients_stringed,
        cooking_time=int(cooking_time)
    )

    recipe_entry.calculate_difficulty(recipe_entry.cooking_time, ingredients)

    # adding and commiting change to database
    session.add(recipe_entry)
    session.commit()
    print('New recipe successfully added')

# a user selects a recipe to delete and deletes if from the table and the database


def view_all_recipes():
    # query to find all recipes in the database
    all_recipes = session.query(Recipe).all()

    # looking to see if there are recipes in the database table, otherwise sends user back to main menu
    if not all_recipes:
        print('No recipes in your database. Returning to main menu.')
        return None

    for recipe in all_recipes:
        print("-" * 35)
        print(recipe.__str__())


def search_by_ingredients():
  # query to count all recipes in the database
    recipe_count = session.query(Recipe).count()

    # looking to see if there are recipes in the database table, otherwise sends user back to main menu
    if recipe_count == 0:
        return None

    # query for just the column in the table that stores ingredients
    results = session.query(Recipe.ingredients).all()

    # initializing empty list
    all_ingredients = []

    for ingredient in results:
        ingredient_string = ingredient[0]
        individualize_ingredient = [i.strip()
                                    for i in ingredient_string.split(',')]
        for i in individualize_ingredient:
            if i not in all_ingredients:
                all_ingredients.append(i)
                print(f'{i} added to your list')
            else:
                print(f'{i} is already on your list!')

    # adds index number to each ingredient in the list
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index}: {ingredient}")

    print('-' * 35)

    # allows user to pick out an ingredient based on its index number
    user_selection = input(
        'Please select number from index of ingredients to find recipes with that ingredient [seperate each number with a space]: ')

    try:
        # converts users input into a list of integers
        selected_ingredients = [int(i) for i in user_selection.strip().split()]
        # convers the integers numbers to ingredients based on their index number
        search_ingredients = [all_ingredients[i] for i in selected_ingredients]

    except ValueError:
        print('Value must be a number. Returning to main menu.')
        return None

    except IndexError:
        print('That index number does not exist in your current index. Returning to main menu.')
        return None

    # initializing empty list
    conditions = []

    # creates a request to the database for the recipes which contain those ingredients and adds it to a list called conditions, which returns a list of those recipes
    for ing in search_ingredients:
        like_term = f'%{ing}%'
        conditions.append(Recipe.ingredients.like(like_term))

    from sqlalchemy import or_

    recipes_with_matching_ingredient = session.query(
        Recipe).filter(or_(*conditions)).all()

    print(
        f'Here are the Recipes containing {", ".join(search_ingredients)}:')
    print(recipes_with_matching_ingredient.__str__())


def edit_recipe():
  # query to count all recipes in the database
    recipe_count = session.query(Recipe).count()

    # looking to see if there are recipes in the database table, otherwise sends user back to main menu
    if recipe_count == 0:
        return None

    # query to find all recipes in the database
    results = session.query(Recipe.id, Recipe.name).all()
    recipe_ids = [row.id for row in results]

    # print out of all the recipes that the user already has stored in database
    print('Here are you recipes in your database: ')
    for row in results:
        print(f"ID: {row.id} | Name: {row.name}")
    print("-" * 35)

    # asks user which recipe they would like to update
    try:
        selected_recipe_id = int(
            input("Please select the ID number of which recipe you would like to update: "))
        if selected_recipe_id not in recipe_ids:
            print('Selection does not match a recipe. Returning to main menu.')
            return None

    except ValueError:
        print('Value must be a number. Returning to main menu')
        return None

    # uses request to select one object from the database
    recipe_to_edit = session.query(Recipe).filter(
        Recipe.id == selected_recipe_id).one()

    # enumerate values from object recipe that was selected
    print('\nWhich field would you like to update')
    print(f'1. Name: {recipe_to_edit.name}')
    print(f'2. Ingredients: {recipe_to_edit.ingredients}')
    print(f'3. Cooking Time: {recipe_to_edit.cooking_time}')

    # asks the user which value of the selected object they would like to update
    try:
        user_input = int(input(
            'Please type the number that corresponds with the field you would like to update: '))
        if user_input not in [1, 2, 3]:
            print('Not a valid input. Please type either 1, 2, or 3.')

    except ValueError:
        print('Value must be a number')
        return None

    # if user selects 2 for ingredients
    if user_input == 2:
        print("Would you like to:")
        print("1 - Add an ingredient")
        print("2 - Remove an ingredient")
        try:
            user_ask = int(input('Enter 1 to add or 2 to remove: '))
        except ValueError:
            print('Value must be a number')
            return None

        # if user selects add
        if user_ask == 1:
            try:
                add_new_ingredient = str(
                    input('Please type the name of the new ingredient you would like to add: '))
            except ValueError:
                print('Value must be a string')
                return None

            # Convert ingredients string to a list
            ingredients_list = [
                i.strip() for i in recipe_to_edit.ingredients.split(",") if i.strip()]

            # Check for duplicates
            if add_new_ingredient in ingredients_list:
                print('Ingredient already in recipe')
            else:
                ingredients_list.append(add_new_ingredient)
                recipe_to_edit.ingredients = ", ".join(ingredients_list)
        # if user selects remove
        elif user_ask == 2:
            try:
                remove_ingredient = str(
                    input('Please type the name of the ingredient you would like to remove: '))
            except ValueError:
                print('Value must be a string')
                return None

            ingredients_list = [
                i.strip() for i in recipe_to_edit.ingredients.split(",") if i.strip()]

            if remove_ingredient not in ingredients_list:
                print('Ingredient not found in this recipe')
            else:
                ingredients_list.remove(remove_ingredient)
                recipe_to_edit.ingredients = ", ".join(ingredients_list)

        else:
            print('Invalid response. Returning to main menu')
            return None

    # if user selects 3 for cooking_time
    elif user_input == 3:
        try:
            new_time = int(input("Enter the new cooking time (in minutes): "))

        except ValueError:
            print('Cooking time must be a number. Returning to main menu')
            return None

        else:
            session.query(Recipe).filter(Recipe.cooking_time == recipe_to_edit.cooking_time).update(
                {Recipe.cooking_time: new_time})

    # if user selects 1 for name
    elif user_input == 1:
        new_name = input("Enter the new name for the recipe: ")
        if len(new_name) > 50:
            print('Name you have selected is not under 50 characters.')
        elif not new_name.isalpha():
            print('Recipe name must only contain letters')
        else:
            session.query(Recipe).filter(
                Recipe.name == recipe_to_edit.name).update({Recipe.name: new_name})

    else:
        print('Selection not valid. Please index that corresponds with either "name", "ingredients", or "cooking_time" ')
        return None

    # recalculating difficulty once function has been udpated
    recipe_to_edit.calculate_difficulty()

    # commiting change to database
    session.commit()
    print('Success! You updated your recipe.')


def delete_recipe():
    # query to find all recipes in the database
    all_recipes = session.query(Recipe).all()

    # looking to see if there are recipes in the database table, otherwise sends user back to main menu
    if not all_recipes:
        print('No recipes in your database. Returning to main menu.')
        return None

    # gives us a list of all recipes which they can delete
    recipe_ids = []

    print('Here are you recipes already created: ')
    for row in all_recipes:
        print(f"ID: {row.id} | Name: {row.name}")
        print("-" * 35)
        recipe_ids.append(row.id)

    # user input for which recipe they would like to delete by id
    try:
        user_selected_id = int(input(
            'Please enter the ID of the recipe that you would like to delete: '))

    # checks for value to be a number
    except ValueError:
        print('Invalid input. Please enter a number')
        return

    # checks to see if id matches one in the database, otherwiese throws an error
    if user_selected_id not in recipe_ids:
        print('That recipe id does not exist')
        return None

    recipe_to_be_deleted = session.query(Recipe).filter(
        Recipe.id == user_selected_id).one()

    # confirms with user that this is the recipe they would like to delete
    user_confirmation = input(
        f'Are you sure you would like to delete your {recipe_to_be_deleted.name} recipe? Please type "yes" or "no". ')
    if user_confirmation == 'no':
        print('Recipe get. Returning you to main menu')
        return None
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
        print("-" * 35)
        print('MAIN MENU')
        print("-" * 35)
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
            search_by_ingredients()
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
