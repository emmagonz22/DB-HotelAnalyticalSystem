import psycopg2

class database:

    def __init__(self, uri):
        self.uri = uri
        self.conn = None
    
    def connect(self):
        if self.conn is None: # if conn is open this not going to connect until disconnected
            try:
                self.conn = psycopg2.connect("dbname='hotelanalyticssystems' user='emmanuel' password='dbproject123456789' host='localhost' port='5432'")
                print("Connected to the database")
            except psycopg2.DatabaseError as e:
                print(f"Database connection failed: {e}")
                raise e
        else:
            print("Database is already connected")
    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            print("Database is disconnected")
        else:
            print("Database is not connected")
