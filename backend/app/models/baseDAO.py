import psycopg2

class BaseDAO:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="test",
            user="postgres",
            password="LosChuletas",
            host="localhost",
            port="5432"
        )