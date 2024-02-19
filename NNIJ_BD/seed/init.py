import random
from faker import Faker
from sqlalchemy.exc import SQLAlchemyError
from database.db import session
from database.models import Teacher, Student, Group, Mark, Subject, TeacherStudent, TeacherSubject, StudentMark, SubjectMark, GroupStudent, GroupTeacher, SubjectStudent

fake = Faker('uk-UA')

def insert_students():
    for _ in range(30):
        student = Student(
            student_name=fake.student_name(),
            created=fake.date_between(start_date='-1y')
        )
        session.add(student)
        
def insert_teachers():
    for _ in range(5):
        teacher = Teacher(
            teacher_name=fake.teacher_name(),
            created=fake.date_between(start_date='-5y')
        )
        session.add(teacher)
        
def insert_subjects():
    for _ in range(5):
        subject = Subject(
            subject_name=fake.subject_name(),
            created=fake.date_between(start_date='-5y')
        )
        session.add(subject)
        
def insert_marks():
    for _ in range(150):
        mark = Mark(
            mark1=fake.mark1(60, 100),
            created1=fake.date_between(start_date='-30d'),
            mark2=fake.mark2(60, 100),
            created2=fake.date_between(start_date='-30d'),
            mark3=fake.mark3(60, 100),
            created3=fake.date_between(start_date='-30d'),
            mark4=fake.mark4(60, 100),
            created4=fake.date_between(start_date='-30d'),
            mark5=fake.mark5(60, 100),
            created5=fake.date_between(start_date='-30d')
        )
        session.add(mark)       

    