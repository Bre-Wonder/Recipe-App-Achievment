import mysql.connector

# initializes connection object
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password'
)

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


all_ingredients = []


def search_recipe(conn, cursor):

    # variable that represents the mySQL command to find the column with just ingredients
    results = 'SELECT * FROM recipes WHERE ingredients'
    for ingredient in results:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
            print(ingredient + ' added to your list')
        else:
            print(ingredient + ' is already on your list!')

    cursor.execute(results)

    # commit changes
    conn.commit()


def update_recipe(conn, cursor):
    cursor.execute('SELECT * from recipes')
    results = cursor.fetchall()

    print('Here are you recipes already created: ')
    for row in results:
        print('ID: ', row[0])
        print('Name: ', row[1])
        print('Ingredients: ', row[2])
        print('Cooking Time in minutes: ', row[3])
        print('Difficulty: ', row[4])

    selected_recipe_id = int(
        input("Please select the number of which recipe you would like to update: "))
    selected_column = input(
        'Which column of your would you like to update name, ingredients, or cooking_time? ')
    updated_value = input(
        'What new value would you like to assign? ')

    if selected_column == 'cooking_time':
        cooking_time = int(updated_value)
        cursor.execute(
            'SLECT cooking_time FROM recipes WHERE id = %s', (selected_recipe_id))
        ingredients = cursor.fetchone()[0].split(', ')
        difficulty = calculate_difficulty(cooking_time, ingredients)

        cursor.execute('UPDATE recipes SET cooking_time = %s, difficulty = %s WHERE id = %s',
                       cooking_time, difficulty, selected_recipe_id)

    elif selected_column == 'ingredients':
        ingredients = cursor.fetchone()[0].split(', ')
        cursor.execute(
            'SLECT ingredients FROM recipes WHERE id = %s', (selected_recipe_id,))
        cooking_time = cursor.fetchone()[0]
        difficulty = calculate_difficulty(cooking_time, ingredients)

        cursor.execute('UPDATE recipes SET ingredients = %s, difficulty = %s WHERE id = %s',
                       ingredients, difficulty, selected_recipe_id)

    else:
        cursor.execute(
            'UPDATE recipes SET {selected_column} = %s WHERE id = %s', (updated_value, selected_recipe_id))

    # commit changes
    conn.commit()
    print('Success! You updated your recipe.')


def delete_recipe(conn, cursor):
    cursor.execute('SELECT * from recipes')
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
    else:
        cursor.execute(
            'DELETE FROM recipes WHERE id = %s', (selected_recipe_id))

    # commit changes
    conn.commit()

    print('Your selected recipe has been deleted')


def main_menu(conn, cursor):
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
        else:
            print('Selection not valid. Please select another number')


main_menu(conn, cursor)
