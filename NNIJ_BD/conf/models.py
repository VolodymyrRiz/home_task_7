from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

# таблиця для зв'язку many-to-many між таблицями notes та tags
# note_m2m_tag = Table(
#     "note_m2m_tag",
#     Base.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("note", Integer, ForeignKey("notes.id", ondelete="CASCADE")),
#     Column("tag", Integer, ForeignKey("tags.id", ondelete="CASCADE")),
# )

# Таблиця вчителів, яка пов*язана зі студентами
class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(150))
    created = Column(DateTime, default=datetime.now())
   
 
 # Таблиця студентів, яка пов*язана з учителями
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    student_name = Column(String(150))
    created = Column(DateTime, default=datetime.now())  
   
   
# Таблиця предметів, яка пов*язана з учителями
class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(200))
    created = Column(DateTime, default=datetime.now())  
    
 # Таблиця оцінок, яка пов*язана зі студентами та предметами
class Mark(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(200))
    created = Column(DateTime, default=datetime.now())     
    
 # Таблиця груп, яка пов*язана зі студентами та вчителями
class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    group_name = Column(String(10))
    created = Column(DateTime, default=datetime.now())   
    
    
    