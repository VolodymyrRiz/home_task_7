from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

# Таблиця вчителів, яка пов*язана зі студентами
class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(150))
    created = Column(DateTime, default=datetime.now())
    students = relationship(argument='Student', secondary='teachers_to_students', back_populates='teachers')
    subjects_teach = relationship(argument='Subject', secondary='teachers_to_subjects', back_populates='teachers_sub')
    group_teach = relationship(argument='Group', secondary='groups_to_teachers', back_populates='teachers_group')
 
 # Таблиця студентів, яка пов*язана з учителями
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    student_name = Column(String(150))
    created = Column(DateTime, default=datetime.now())  
    teachers = relationship(argument='Teacher', secondary='teachers_to_students', back_populates='students')
    marks = relationship(argument='Mark', secondary='students_to_marks', back_populates='studentsmarks')
    groups = relationship(argument='Group', secondary='groups_to_students', back_populates='studgroup')
    subjstud = relationship(argument='Subject', secondary='subjects_to_students', back_populates='studsubj')
    
    
   
# # Таблиця предметів, яка пов*язана з учителями
class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(200))
    created = Column(DateTime, default=datetime.now())  
    teachers_sub = relationship(argument='Teacher', secondary='teachers_to_subjects', back_populates='subjects_teach')
    marks_sub = relationship(argument='Mark', secondary='subjects_to_marks', back_populates='subjectsmarks')
    studsubj = relationship(argument='Student', secondary='subjects_to_students', back_populates='subjstud')
    
#  # Таблиця оцінок, яка пов*язана зі студентами та предметами
class Mark(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True)
    nark1 = Column(Integer)
    created1 = Column(DateTime, default=datetime.now()) 
    mark2 = Column(Integer)
    created2 = Column(DateTime, default=datetime.now())
    mark3 = Column(Integer)
    created3 = Column(DateTime, default=datetime.now())
    mark4 = Column(Integer)
    created4 = Column(DateTime, default=datetime.now())
    mark5 = Column(Integer)
    created5 = Column(DateTime, default=datetime.now())
    studentsmarks = relationship(argument='Student', secondary='students_to_marks', back_populates='marks')
    subjectsmarks = relationship(argument='Subject', secondary='subjects_to_marks', back_populates='marks_sub')
    
#  # Таблиця груп, яка пов*язана зі студентами та вчителями
class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    group_name = Column(String(10))
    created = Column(DateTime, default=datetime.now())   
    studgroup = relationship(argument='Student', secondary='groups_to_students', back_populates='groups')
    teachers_group = relationship(argument='Teacher', secondary='groups_to_teachers', back_populates='group_teach')
    
 # Таблиці зв*язків ---------------------   
class TeacherStudent(Base):    
    __tablename__ = "teachers_to_students"
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE', onupdate='CASCADE'))
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'))
    
  
class TeacherSubject(Base):    
    __tablename__ = "teachers_to_subjects"
    id = Column(Integer, primary_key=True)
    teachersub_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE', onupdate='CASCADE'))
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete='CASCADE', onupdate='CASCADE'))
      
      
class StudentMark(Base):    
    __tablename__ = "students_to_marks"
    id = Column(Integer, primary_key=True)
    studentmark_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'))
    markstud_id = Column(Integer, ForeignKey('marks.id', ondelete='CASCADE', onupdate='CASCADE'))
    
    
class SubjectMark(Base):    
    __tablename__ = "subjects_to_marks"
    id = Column(Integer, primary_key=True)
    subjmark_id = Column(Integer, ForeignKey('subjects.id', ondelete='CASCADE', onupdate='CASCADE'))
    marksubj_id = Column(Integer, ForeignKey('marks.id', ondelete='CASCADE', onupdate='CASCADE'))
    
    
class GroupStudent(Base):    
    __tablename__ = "groups_to_students"
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.id', ondelete='CASCADE', onupdate='CASCADE'))
    groupstud_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'))
    
    
class GroupTeacher(Base):    
    __tablename__ = "groups_to_teachers"
    id = Column(Integer, primary_key=True)
    groupteach_id = Column(Integer, ForeignKey('groups.id', ondelete='CASCADE', onupdate='CASCADE'))
    teachgroup_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE', onupdate='CASCADE'))
    
    
class SubjectStudent(Base):    
    __tablename__ = "subjects_to_students"
    id = Column(Integer, primary_key=True)
    subjstud_id = Column(Integer, ForeignKey('subjects.id', ondelete='CASCADE', onupdate='CASCADE'))
    studsubj_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'))

