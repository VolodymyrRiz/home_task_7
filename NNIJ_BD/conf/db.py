import configparser

import pathlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2

import faker

# URI: postgresql://username:password@domain:port/database

file_config = pathlib.Path(__file__).parent.parent.joinpath("config.ini")

config = configparser.ConfigParser()
config.read(file_config)

user = config.set('DEV_DB', )
password = config.set('PASSWORD', 'nnij2024')
domain = config.set('DOMAIN', 'localhost')
port = config.set('PORT', '5432')
db = config.set('DB_NAME', 'nnij_pg')

URI = f'postgresql://{user}:{password}@{domain}:{port}/{db}'


print(URI)

