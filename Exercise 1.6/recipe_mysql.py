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
