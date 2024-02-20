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


from models import Teacher, Student, Group, Mark, Subject, TeacherStudent, TeacherSubject, StudentMark, SubjectMark, GroupStudent, GroupTeacher, SubjectStudent

fake = faker.Faker()

def insert_students():
    for _ in range(30):
        student = Student(
            student_name=fake.name(),
            created=fake.date_between(start_date='-1y')
        )
        session.add(student)
        
def insert_teachers():
    for _ in range(5):
        teacher = Teacher(
            teacher_name=fake.name(),
            created=fake.date_between(start_date='-5y')
        )
        session.add(teacher)
        
def insert_subjects():
    for _ in range(5):
        subject = Subject(
            subject_name=fake.job(),
            created=fake.date_between(start_date='-5y')
        )
        session.add(subject)
        
def insert_marks():
    for _ in range(150):
        mark = Mark(
            nark1=random.randrange(60, 100),
            created1=fake.date_between(start_date='-30d'),
            mark2=random.randrange(60, 100),
            created2=fake.date_between(start_date='-30d'),
            mark3=random.randrange(60, 100),
            created3=fake.date_between(start_date='-30d'),
            mark4=random.randrange(60, 100),
            created4=fake.date_between(start_date='-30d'),
            mark5=random.randrange(60, 100),
            created5=fake.date_between(start_date='-30d')
        )
        session.add(mark)   
        
        
def insert_groups():
    for a in range(3):
        group = Group(
            group_name=str(a),
            created=fake.date_between(start_date='-1y')
        )
        session.add(group)    

def insert_rel1():   
    students = session.query(Student).all()
    teachers = session.query(Teacher).all()
    
    # teachersubs = session.query(Teacher).all()
    # subjects = session.query(Subject).all()
    
    # studentmarks = session.query(Student).all()
    # markstuds = session.query(Mark).all()
    
    # subjmarks = session.query(Subject).all()
    # marksubjs = session.query(Mark).all()
    
    # groups = session.query(Group).all()
    # groupstuds = session.query(Student).all()
    
    # groupteachs = session.query(Group).all()
    # teachgroups = session.query(Teacher).all()
    
    # subjstuds = session.query(Subject).all()
    # studsubjs = session.query(Student).all()
    
    for student in students:
        rel = TeacherStudent(teacher_id=random.choice(teachers).id, student_id=student.id)
        
    # for subject in subjects:
    #     rel = TeacherSubject(teachersub_id=random.choice(teachersubs).id, subject_id=subject.id)
        
    # for studentmark in studentmarks:
    #     rel = StudentMark(markstud_id=random.choice(markstuds).id, studentmark_id=studentmark.id)    
        
    # for subjmark in subjmarks:
    #     rel = SubjectMark(marksubj_id=random.choice(marksubjs).id, subjmark_id=subjmark.id)
        
    # for group in groups:
    #     rel = GroupStudent(groupstud_id=groupstuds.id, group_id=group.id)
        
    # for groupteach in groupteachs:
    #     rel = GroupTeacher(teachgroup_id=random.choice(teachgroups).id, groupteach_id=groupteach.id)
        
    # for subjstud in subjstuds:
    #     rel = SubjectStudent(studsubj_id=random.choice(studsubjs).id, subjstud_id=subjstud.id)   
   
        
        
if __name__ == '__main__':
    session = Session()   
    
    try:
        insert_students()
        insert_teachers()
        insert_subjects()
        insert_marks()
        insert_groups()
        session.commit()
        insert_rel()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()