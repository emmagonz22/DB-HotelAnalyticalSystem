import psycopg2

class database:

    def __init__(self, host,
                username,
                password, 
                dbname, 
                port):
        self.host = host
        self.username = username
        self.password = password
        self.dbname = dbname
        self.port = port
        self.conn = None
    
    def connect(self):
        if self.conn is None: # if conn is open this not going to connect until disconnected
            try:
                self.conn = psycopg2.connect(f"dbname={self.dbname} user={self.username} password={self.password} host={self.host} port={self.port}")
                print("Connected to the database")
            except psycopg2.DatabaseError as e:
                print(f"Database connection failed: {e}")
                raise e
        else:
            print("Database is already connected")
    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
        else:
            print("Database is not connected")
