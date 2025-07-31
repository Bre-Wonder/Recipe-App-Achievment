import mysql.connector

# initializes connection object
conn = mysqul.connector.connect(
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
        print('Type 'quit' to exit the program')
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


def create_recipe(conn, cursor):


def search_recipe(conn, cursor):


def update_recipe(conn, cusor):


def delete_recipe(conn, cursor):
