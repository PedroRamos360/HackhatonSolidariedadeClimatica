import os
import sys
import mariadb
import dotenv

dotenv.load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_URL = os.getenv("DB_URL")


def create_db_tables():
    db = Database()
    db.execute_query(
        """
        CREATE TABLE IF NOT EXISTS shelters 
        (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            name VARCHAR(255),
            description TEXT,
            latitude FLOAT,
            longitude FLOAT,
            link_to_donate VARCHAR(255) 
        )
        """
    )
    db.close()


class Database:
    def __init__(self):
        self.connection = self.__get_connection()

    def __get_connection(self):
        return mariadb.connect(
            user=DB_USER, password=DB_PASS, host=DB_URL, port=3306, database="hackaton"
        )

    def execute_query(self, query: str):
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)

    def close(self):
        self.connection.close()
