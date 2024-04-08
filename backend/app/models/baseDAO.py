import psycopg2
import os

from dotenv import load_dotenv
from pathlib import Path


dotenv_path = os.path.abspath("app/enviroment.env")
load_dotenv(dotenv_path=dotenv_path)

class BaseDAO:

    def __init__(self):

        self.conn = psycopg2.connect(
            database=os.getenv('DATABASE'),
            user=os.getenv('USER_DB'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
        )
        

