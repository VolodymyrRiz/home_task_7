from datetime import datetime
import faker
import random
from random import randint, choice
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 5
NUMBER_MARKS = 150


def generate_fake_data(number_groups, number_students, number_teachers, number_subjects, number_marks) -> tuple():
    fake_groups = []  # тут зберігатимемо групи
    fake_students = []  # тут зберігатимемо сстудентів
    fake_teachers = []  # тут зберігатимемо вчителів
    fake_subjects = []  # тут зберігатимемо дисципліни
    fake_marks = []  # тут зберігатимемо оцінки
    '''Візьмемо три групи з faker і помістимо їх у потрібну змінну'''
    fake_data = faker.Faker()

    # Створимо набір груп у кількості number_groups
    for er in range(number_groups):
        fake_groups.append(str(er))

    # Згенеруємо тепер number_students кількість студентів'''
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Та number_teachers набір вчителів
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())
        
     # Згенеруємо тепер number_subjects кількість дисциплін'''
    for _ in range(number_subjects):
        fake_subjects.append(fake_data.job())

    # Та number_marks набір оцінок
        
    for _ in range(number_marks):
        mrk = random.randint(60, 100)
        fake_marks.append(mrk)

    return fake_groups, fake_students, fake_teachers, fake_subjects, fake_marks


def prepare_data(grups_nnij, student_nnij, teacher_nnij, subject_nnij, mark_nnij) -> tuple():
    for_groups = []
    # готуємо список кортежів назв груп
    for name_ in grups_nnij:
        for_groups.append((name_))

    for_students = []  # для таблиці students_nnij
    for student in student_nnij:
       for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_teachers = [] # для таблиці teachers_nnij
    for teacher in teachers_nnij:
        for_teachers.append((teacher, randint(1, NUMBER_GROUPS)))
        
    for_subjects = [] # для таблиці subjects_nnij     
    for subject_ in subject_nnij:
        for_subjects.append((subject_, randint(1, NUMBER_TEACHERS)))
        
    for_marks = [] # для таблиці marks_nnij   
    ns = 1
    ns1 = 1
    nd = 1
    nd1 = 1
    for mark in mark_nnij:
        
        if ns == NUMBER_SUBJECTS + 1:
            ns = 1
            ns1 = ns1 + 1
        if nd == NUMBER_SUBJECTS + 1:
            nd = 1
            nd1 = 1
        for_marks.append((ns1, nd1, mark))
        ns += 1
        nd += 1
        nd1 += 1
    
    return  grups_nnij, for_students, for_teachers, for_subjects, for_marks


def insert_data_to_db(grups_nnij, student_nnij, teacher_nnij, subject_nnij, mark_nnij) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними    
    with sqlite3.connect('nnij_new1.db') as con:

        cur = con.cursor()

        '''Заповнюємо таблицю груп. І створюємо скрипт для вставлення, де змінні, які вставлятимемо, відзначимо
        знаком заповнювача (?) '''

        sql_to_groups_nnij = """INSERT INTO groups_nnij(name_)
                               VALUES (?)"""

        '''Для вставлення відразу всіх даних скористаємося методом executemany курсора. Першим параметром буде текст
        скрипта, а другим - дані (список кортежів).'''

        cur.executemany(sql_to_groups_nnij, groups_nnij)

        # Далі вставляємо дані про студентів. Напишемо для нього скрипт і вкажемо змінні

        sql_to_students_nnij = """INSERT INTO students_nnij(student, groups_nnij_id)
                               VALUES (?, ?)"""

        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(sql_to_students_nnij, student_nnij)
        
        
        sql_to_teachers_nnij = """INSERT INTO teachers_nnij(teacher, groups_nnij_id)
                               VALUES (?, ?)"""

        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(sql_to_teachers_nnij, teacher_nnij)
        
        
        sql_to_subjects_nnij = """INSERT INTO subjects_nnij(subject_, teachers_nnij_id)
                               VALUES (?, ?)"""

        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(sql_to_subjects_nnij, subject_nnij)         
        

        # Останньою заповнюємо таблицю 

        sql_to_marks_nnij = """INSERT INTO marks_nnij(students_nnij_id, subjects_nnij_id, mark)
                              VALUES (?, ?, ?)"""

        # Вставляємо дані про зарплати

        cur.executemany(sql_to_marks_nnij, mark_nnij)

        # Фіксуємо наші зміни в БД

        con.commit()


if __name__ == "__main__":
    grups_nnij, student_nnij, teacher_nnij, subject_nnij, mark_nnij = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_SUBJECTS, NUMBER_MARKS))
    insert_data_to_db(grups_nnij, student_nnij, teacher_nnij, subject_nnij, mark_nnij)
