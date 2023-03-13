import models
from models.database import engine, Session, Base
from models.employeer import Employeer
from models.create_database import *
import random 
import contextlib
db = Session()
connection = engine.connect()

def add_new_employer(base=Employeer, full_name="Иванов Иван", age=random.randint(18, 50)):
    db.add(Employeer(full_name, age))
    db.commit()

def reset_database():
    Base.metadata.drop_all(engine)
    create_database()

# print(connection.execute('SELECT * FROM employeer').fetchall())
