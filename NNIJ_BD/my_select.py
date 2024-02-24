from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func
from sqlalchemy import func, desc
from connect_db import session
from models import Teacher, Student, Group, Rating, Subject
from models import SessionLocal

# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1():
    q1 = session.query(Student.stud_name, func.round(func.avg(Rating.grade), 2).label('avg_grade'))\
        .select_from(Rating).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return q1

# Знайти студента із найвищим середнім балом з певного предмета.
def select_2():
    q2 = session.query(Student.stud_name, func.round(func.avg(Rating.grade), 2).label('avg_grade'))\
        .select_from(Rating).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(1).all()
    return q2

# Знайти середній бал у групах з певного предмета.
def select_3():
    q3 = session.query(Student.group_id, func.round(func.avg(Rating.grade), 2).label('avg_grade'))\
        .select_from(Rating).join(Student).group_by(Student.group_id).order_by(desc('avg_grade')).all()
    return q3

# Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4():
    q4 = session.query(func.round(func.avg(Rating.grade), 2)).all()
    return q4

# Знайти які курси читає певний викладач.
def select_5():
    q5 = session.query(Teacher.teach_name.label('teacher'), Subject.subj_name.label('subject'))\
        .select_from(Teacher).join(Subject).all()        
    return q5

# Знайти список студентів у певній групі.
def select_6():
    q6 = session.query(Student.stud_name.label('student'), Student.group_id)\
        .select_from(Student).order_by(Student.group_id).all()   
    return q6

# Знайти оцінки студентів у окремій групі з певного предмета.
def select_7():
    q7 = session.query(Group.gr_name.label('group'), Student.stud_name.label('student'),\
        Rating.subject_id.label('subject'), Rating.grade.label('grade'))\
        .select_from(Rating).join(Student).join(Group)\
        .limit(150).all()
    return q7

# Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8():
    q8 = session.query(Subject.subj_name, func.round(func.avg(Rating.grade), 2).label('avg_grade'))\
        .select_from(Subject).join(Rating).group_by(Subject.id).all()
    return q8

# Знайти список курсів, які відвідує певний студент.
def select_9():
    q9 = session.query(Subject.subj_name.label('subject'), Student.stud_name.label('student'))\
        .select_from(Rating).join(Student).join(Subject).join(Teacher).limit(150).all()
    return q9

# Список курсів, які певному студенту читає певний викладач.
def select_10():
    q10 = session.query(Subject.subj_name.label('subject'), Teacher.teach_name.label('teacher'), Student.stud_name.label('student'))\
        .select_from(Rating).join(Student).join(Subject).join(Teacher).limit(150).all()
    return q10


if __name__ == '__main__':
    db = SessionLocal()
    print('')
    z = 1
    print('ВИКОНАНО ЗАПИТ ', z)
    print(select_1())
    print('')
    z = 2
    print('ВИКОНАНО ЗАПИТ ', z)
    print(select_2())
    print('')
    z = 3
    print('ВИКОНАНО ЗАПИТ ', z)
    print(select_3())
    print('')
    z = 4
    print('ВИКОНАНО ЗАПИТ ', z)
    print(select_4())
    print('')
    z = 5
    print('ВИКОНАНО ЗАПИТ ', z)
    print(select_5())
    print('')
    z = 6
    print('ВИКОНАНО ЗАПИТ ', z)
    print(select_6())
    print('')
    z = 7
    print('ВИКОНАНО ЗАПИТ ', z)
    print(select_7())
    print('')
    z = 8
    print('ВИКОНАНО ЗАПИТ ', z)
    print(select_8())
    print('')
    z = 9
    print('ВИКОНАНО ЗАПИТ ', z)
    print(select_9())
    print('')
    z = 10
    print('ВИКОНАНО ЗАПИТ ', z)
    print(select_10())
    print('')
    
    db.commit()
    db.close()
   
