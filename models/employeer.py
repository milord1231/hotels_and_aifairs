from sqlalchemy import Column, Integer, String, ForeignKey
from models.database import Base


class Employeer(Base):
    __tablename__ = 'employeer'

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    age = Column(Integer)

    def __init__(self, full_name: str, age: int):
        full_name = full_name.split()
        self.surname = full_name[0]
        self.name = full_name[1]
        self.age = age

    def __repr__(self):
         def __repr__(self):
          return '<employeer %r>' % self.id