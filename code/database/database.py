# database.py

import psycopg2

class Database:
    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
    
    def execute(self, query, *args):
        try:
            cur = self.conn.cursor()
            cur.execute(query, *args)
            self.conn.commit()
            cur.close()
        except Exception as e:
            print(f"Error: {e}")

    def fetch(self, query, *args):
        try:
            cur = self.conn.cursor()
            cur.execute(query, *args)
            results = cur.fetchall()
            cur.close()
            return results
        except Exception as e:
            print(f"Error: {e}")

    def fetch_one(self, query, params=None):
        with self.conn.cursor() as cur:
            cur.execute(query, params)
            result = cur.fetchone()
        return result