from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:nnij2024@localhost:5432/nnij_pgbase1")
Session = sessionmaker(bind=engine)
session = Session()
