import random
import faker
from alembic import context
from sqlalchemy import pool
from sqlalchemy import Column, Integer, String, Boolean

from sqlalchemy.orm import Session
import datetime
from datetime import datetime, timedelta

import pathlib
from pathlib import Path
from sqlalchemy.sql import select

#from sqlalchemy.orm import choice
from sqlalchemy.orm import sessionmaker

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import session

from models import Teacher, Student, Group, Rating, Subject

from sqlalchemy.orm import Session

from models import SessionLocal

fake = faker.Faker()


def date_range(start, end) -> list:
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result

def insert_group():
    for a in range(3):
        group = Group(gr_name=str(a))
        db.add(group)
    db.commit()
    
def insert_student():
    group_id_select = db.scalars(select(Group.id)).all()
    for _ in range(30):
        random_id_group = random.choice(group_id_select)
        student = Student(
            stud_name=fake.name(),
            group_id = random_id_group,
            )
        db.add(student)
    db.commit()

def insert_teacher():
    for _ in range(5):
        teacher = Teacher(teach_name=fake.name())
        db.add(teacher)
    db.commit()    
  
def insert_subject():
    teacher_id_select = db.scalars(select(Teacher.id)).all()
    for _ in range(5):
        random_id_teacher = random.choice(teacher_id_select)
        subject = Subject(
            subj_name=fake.name(),
            teacher_id = random_id_teacher,
            )
        db.add(subject)
    db.commit()    
    
def insert_grade():
    start_date = datetime.strptime("2023-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2024-02-14", "%Y-%m-%d")
    d_range = date_range(start=start_date, end=end_date)
    discipline_id_select = db.scalars(select(Subject.id)).all()
    student_id_select = db.scalars(select(Student.id)).all()

    for d in d_range:
        random_id_discipline = random.choice(discipline_id_select)
        random_ids_student = [random.choice(student_id_select) for _ in range(150)]
        for student_id in random_ids_student:
            grade = Rating(
                grade=random.randrange(1, 100),
                date_of=d,
                student_id=student_id,
                subject_id=random_id_discipline,
            )
            db.add(grade)
    db.commit()       
        
if __name__ == '__main__':
    db = SessionLocal() 

try:
    insert_group()
    insert_student()
    insert_teacher()
    insert_subject()
    insert_grade()    
    db.commit()
   
except SQLAlchemyError as e:
    print(e)
    db.rollback()
finally:
    db.close()