import psycopg2
from psycopg2.extras import RealDictCursor

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='gpp_db',
            user='josemng',
            password='anot2381fG',
            host='localhost',
            port=5432
        )
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)

    def query(self, query, args=None):
        self.cursor.execute(query, args)
        return self.cursor.fetchall()

    def execute(self, query, args=None):
        self.cursor.execute(query, args)
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()
