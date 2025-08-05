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

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + "Difficulty Level: " + str(self.difficulty) + ">"

    def __str__

    # Come back to this one
    def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = 'Easy'
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = 'Medium'
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = 'Intermediate'
    elif cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = 'Hard'
    return self.difficulty


Base.metadata.create_all(engine)
