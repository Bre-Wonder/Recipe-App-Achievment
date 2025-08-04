import mysql.connector

# initializes connection object
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password'
)

all_ingredients = []

cursor = conn.cursor()

# creates database
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
# selects database
cursor.execute("USE task_database")
# creating a table
cursor.execute('''CREATE TABLE IF NOT EXISTS recipes(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  ingredients VARCHAR(255),
  cooking_time INT,
  difficulty VARCHAR(20)
)''')


def create_recipe(conn, cursor):
    recipe_name = str(input("Please give the name of the recipe here: "))
    cooking_time = int(input("Please give the cooking time in minutes: "))
    ingredients = input(
        "Please list your ingredients here (please note to put a comma between each ingredient): ").split(', ')
    difficulty = calculate_difficulty(cooking_time, ingredients)

    stringed_ingredients = ", ".join(ingredients)

    # executing command for inputs to go into MySQL database - recipes
    sql = 'INSERT INTO recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    values = (recipe_name, stringed_ingredients, cooking_time, difficulty)
    cursor.execute(sql, values)

    print('Your recipe has been created and added')

    # committing changes
    conn.commit()


def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = 'Easy'
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = 'Medium'
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = 'Intermediate'
    elif cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = 'Hard'
    return difficulty


def search_recipe(conn, cursor):

    cursor.execute('SELECT ingredients FROM recipes')
    results = cursor.fetchall()

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

    # allows user to pick out an ingredient based on its index number
    try:
        search_ingredient = int(input(
            'Please select number from index of ingredients: '))

    except ValueError:
        print('Value must be a number')

    except IndexError:
        print('That index number does not exist in you current index')

    # if no errors are found, gives a list of recipes that have the selected ingredient in it

    output = all_ingredients[search_ingredient]
    matching_recipe = []

    cursor.execute('SELECT name, ingredients FROM recipes')
    recipe_data = cursor.fetchall()

    for name, ingredient_string in recipe_data:
        if output.lower() in ingredient_string.lower():
            matching_recipe.append(name)

    if matching_recipe:
        print(f'Recipes conataining "{output}": ')
        for name in matching_recipe:
            print(f"- {name}")
    else:
        print('No recipes contain this ingredient')

    # commit changes
    conn.commit()


def update_recipe(conn, cursor):
    cursor.execute('SELECT * FROM recipes')
    results = cursor.fetchall()

    # prints out a list of alreayd existing recipes so the user knows what they can choose from
    print('Here are you recipes already created: ')
    for row in results:
        print('ID: ', row[0])
        print('Name: ', row[1])
        print('Ingredients: ', row[2])
        print('Cooking Time in minutes: ', row[3])
        print('Difficulty: ', row[4])

    # user selects updates by answering input questions
    try:
        selected_recipe_id = int(
            input("Please select the number of which recipe you would like to update: "))
    except ValueError:
        print('Invalid input for recipe ID')
        return

    selected_column = input(
        'Which column of your would you like to update name, ingredients, or cooking_time? ')

    if selected_column not in ['name', 'ingredients', 'cooking_time']:
        print('Invalid selection for column')
        return

    updated_value = input(
        'What new value would you like to assign? ')

    if selected_column == 'cooking_time':
        try:
            cooking_time = int(updated_value)
        except ValueError:
            print('Cooking time must be an integer number')
            return

        cursor.execute(
            'SELECT ingredients FROM recipes WHERE id = %s', (selected_recipe_id,))
        result = cursor.fetchone()
        if not result:
            print('Not recipe found with that ID')
            return

        ingredients = result[0].split(', ')
        difficulty = calculate_difficulty(cooking_time, ingredients)

        cursor.execute('UPDATE recipes SET cooking_time = %s, difficulty = %s WHERE id = %s',
                       (cooking_time, difficulty, selected_recipe_id))

    elif selected_column == 'ingredients':
        ingredients_list = updated_value.split(', ')
        cursor.execute(
            'SELECT cooking_time FROM recipes WHERE id = %s', (selected_recipe_id,))
        result = cursor.fetchone()
        if not result:
            print('Not recipe found with that ID')
            return

        cooking_time = result[0]
        difficulty = calculate_difficulty(cooking_time, ingredients_list)

        cursor.execute('UPDATE recipes SET ingredients = %s, difficulty = %s WHERE id = %s',
                       (updated_value, difficulty, selected_recipe_id))

    else:
        sql = 'UPDATE recipes SET name = %s WHERE id = %s'
        cursor.execute(sql, (updated_value, selected_recipe_id,))

    # commit changes
    conn.commit()
    print('Success! You updated your recipe.')


def delete_recipe(conn, cursor):
    cursor.execute('SELECT * FROM recipes')
    results = cursor.fetchall()
    recipe_ids = []

    print('Here are you recipes already created: ')
    for row in results:
        print('ID: ', row[0])
        print('Name: ', row[1])
        print('Ingredients: ', row[2])
        print('Cooking Time in minutes: ', row[3])
        print('Difficulty: ', row[4])
        recipe_ids.append(row[0])

    try:
        selected_recipe_id = int(
            input("Please select the number of which recipe you would like to delete: "))
    except ValueError:
        print('Invalid input. Please enter a number')
        return

    if selected_recipe_id not in recipe_ids:
        print('That recipe id does not exist')
        return

    cursor.execute('SELECT name FROM recipes WHERE id = %s',
                   (selected_recipe_id,))
    result = cursor.fetchone()
    if result:
        recipe_name = result[0]

    else:
        print('Recipe not found')

    selected_delete = 'DELETE FROM recipes WHERE id = %s'
    cursor.execute(selected_delete, (selected_recipe_id,))

    # commit changes
    conn.commit()

    print(f'"{recipe_name}" recipe has been deleted')


def main_menu(conn, cursor):
    choice = ''
    while (choice != 'quit'):
        print('MAIN MENU')
        print('----------------------')
        print('----------------------')
        print('What would you like to do? Pick a number that corresponds with the option you would like to select')
        print('1. Create a recipe')
        print('2. Search for a recipe')
        print('3. Update a recipe')
        print('4. Delete a recipe')
        print("Type 'quit' to exit the program")
        choice = input('Your Choice: ')

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == 'quit':
            print('You selected quit. Program has stopped.')
        else:
            print('Selection not valid. Please select another number')


main_menu(conn, cursor)
