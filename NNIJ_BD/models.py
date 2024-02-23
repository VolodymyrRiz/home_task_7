from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
Base = declarative_base()

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:nnij2024@localhost:5432/nnij_pgbase1"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    teach_name = Column(String(250), nullable=False)
    
class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    gr_name = Column(String(20), nullable=False)
    
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    stud_name = Column(String(120), nullable=False)
    group_id = Column('group_id', ForeignKey('groups.id', ondelete='CASCADE'))
    group = relationship('Group', backref='students')
    
class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    subj_name = Column(String(250), nullable=False)
    teacher_id = Column('teacher_id', ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher = relationship("Teacher", backref="subjects")
    
class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    date_of = Column('date_of', Date, nullable=True)
    grade = Column(Integer, nullable=False)   
    student_id = Column("student_id", ForeignKey("students.id", ondelete="CASCADE"))
    student = relationship('Student', backref='ratings')
    subject_id = Column("subject_id", ForeignKey("subjects.id", ondelete="CASCADE"))
    subject = relationship('Subject', backref='ratings') 