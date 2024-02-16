#import create_db
# import fill_data

import sqlite3
import os
from pathlib import Path


# def create():
#     create_db.run()
#     pass


# def fill_data():
#     fill_data.run()
#     pass


def query(number):
    file = 'query' + number + '.sql'
    with open(file, 'r') as f:
        sql = f.read()       
    with sqlite3.connect('nnij_new1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()          
 

if __name__ == "__main__":
    number = ''
    #create()
    #fill_data()
    while True:
        print('Виберіть номер запиту: ')
        print('Знайти 5 студентів із найбільшим середнім балом з усіх предметів - 1 + Enter')
        print('Знайти студента із найвищим середнім балом з певного предмета - 2 + Enter')
        print('Знайти середній бал у групах з певного предмета - 3 + Enter')
        print('Знайти середній бал на потоці (по всій таблиці оцінок) - 4 + Enter')
        print('Знайти які курси читає певний викладач - 5 + Enter')
        print('Знайти список студентів у певній групі - 6 + Enter')
        print('Знайти оцінки студентів у окремій групі з певного предмета - 7 + Enter')
        print('Знайти середній бал, який ставить певний викладач зі своїх предметів - 8 + Enter')
        print('Знайти список курсів, які відвідує студент - 9 + Enter')
        print('Список курсів, які певному студенту читає певний викладач - 10 + Enter')
        print('Припинити запити - 0 + Enter')    
        number = str(input())       
        if number == '0':
            os.abort()
        print('Р Е З У Л Ь Т А Т______________________')
        print(query(number))
        print('')
        print('')
        print('ПРОДОВЖИТИ - Enter')
        input()
        print('')
        continue
                