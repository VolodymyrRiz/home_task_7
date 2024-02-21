import random
import faker
from alembic import context
from sqlalchemy import pool
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import pathlib
from pathlib import Path

from sqlalchemy.orm import sessionmaker

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import session


from models import Teacher, Student, Group, Rating, Subject

fake = faker.Faker()


def insert_teacher():
    for _ in range(5):
        teacher = Teacher(teach_name=fake.name())
        session.add(teacher)
    session.commit()
    
def insert_student():
    for _ in range(30):
        student = Student(stud_name=fake.name())
        session.add(student)
    session.commit()
    
def insert_subject():
    for _ in range(5):
        subject = Subject(subj_name=fake.name())
        session.add(subject)
    session.commit()
    
def insert_group():
    for a in range(3):
        group = Group(gr_name=str(a))
        session.add(group)
    session.commit()
    
def insert_grade():
    for _ in range(150):
        grade = Rating(random.randrange(60, 100))
        session.add(grade)
    session.commit()
    
    
if __name__ == '__main__':
    session = Session()   

try:
    insert_student()
    insert_teacher()
    insert_subject()
    insert_grade()
    insert_group()
    session.commit()
   
except SQLAlchemyError as e:
    print(e)
    session.rollback()
finally:
    session.close()