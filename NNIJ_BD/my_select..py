from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import func, desc
from connect_db import session
from models import Teacher, Student, Group, Rating, Subject

# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1():
    session.query(Student.stud_name, func.round(func.avg(Rating.grade), 2).label('avg_grade'))\
        .select_from(Rating).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    

# Знайти студента із найвищим середнім балом з певного предмета.
def select_2():
    pass

# Знайти середній бал у групах з певного предмета.
def select_3():
    pass

# Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4():
    pass

# Знайти які курси читає певний викладач.
def select_5():
    pass

# Знайти список студентів у певній групі.
def select_6():
    pass

# Знайти оцінки студентів у окремій групі з певного предмета.
def select_7():
    pass

# Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8():
    pass

# Знайти список курсів, які відвідує певний студент.
def select_9():
    pass

# Список курсів, які певному студенту читає певний викладач.
def select_10():
    pass


if __name__ == '__main__':
    print(select_1())
    #q = session.execute(select(Teacher))
        # .join(Group)
        # .join(Student)
        # .join(Subject)
        # .join(Teacher)
        # .join(Rating)
        
        # .join(Tag).filter(Tag.name == 'food')
        #   ).mappings().all()
        
    # for row in q:
    #     print(row)
        #users.append(row)
    # for user in q.scalars():
    #     print(user.id, user.teach_name)
    #print(q)
