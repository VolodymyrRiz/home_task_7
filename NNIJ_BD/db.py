import configparser

import pathlib
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
import faker

# URI: postgresql://username:password@domain:port/database

file_config = pathlib.Path(__file__).parent.parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)

user = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
db = config.get('DEV_DB', 'DB_NAME')
domain = config.get('DEV_DB', 'DOMAIN')
port = config.get('DEV_DB', 'PORT')

URI = f'postgresql://{user}:{password}@{domain}:{port}/{db}'

engine = create_engine(URI, echo=False, pool_size=5, max_overflow=0)
DBsession = sessionmaker(bind=engine)
session = DBsession()

