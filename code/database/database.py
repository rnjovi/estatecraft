import psycopg2

class Database:
    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        """
        Initialize a connection to the database.

        :param dbname: Database name
        :param user: Username for the database
        :param password: Password for the database
        :param host: Host where the database is running (default: "localhost")
        :param port: Port for the database connection (default: "5432")
        """
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
    
    def execute(self, query, *args):
        """
        Execute a query on the database.

        :param query: SQL query string
        :param args: Optional query parameters
        """
        try:
            cur = self.conn.cursor()
            cur.execute(query, *args)
            self.conn.commit()
            cur.close()
        except Exception as e:
            print(f"Error: {e}")

    def fetch(self, query, *args):
        """
        Execute a query and fetch all results.

        :param query: SQL query string
        :param args: Optional query parameters
        :return: List of results
        """
        try:
            cur = self.conn.cursor()
            cur.execute(query, *args)
            results = cur.fetchall()
            cur.close()
            return results
        except Exception as e:
            print(f"Error: {e}")

    def fetch_one(self, query, params=None):
        """
        Execute a query and fetch the first result.

        :param query: SQL query string
        :param params: Optional query parameters
        :return: First result of the query
        """
        with self.conn.cursor() as cur:
            cur.execute(query, params)
            result = cur.fetchone()
        return result