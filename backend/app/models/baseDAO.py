import psycopg2
import os

from dotenv import load_dotenv
from pathlib import Path


# dotenv_path = os.path.abspath("backend/app/enviroment.env")
dotenv_path = os.path.abspath("app/enviroment_prod.env")
print(dotenv_path)
load_dotenv(dotenv_path=dotenv_path)

class BaseDAO:

    def __init__(self):
        print( os.getenv('DATABASE'),
            os.getenv('USER_DB'),
            os.getenv('PASSWORD'),
            os.getenv('HOST'),
            os.getenv('PORT'),
            os.getenv('PORT_P'))
        self.conn = psycopg2.connect(
            database=os.getenv('DATABASE'),
            user=os.getenv('USER_DB'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT_P')
        )
        

