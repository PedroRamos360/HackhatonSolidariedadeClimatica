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
    db.update_query(
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
        self.__connection = self.__get_connection()
        self.__cursor = self.__connection.cursor()

    def __get_connection(self):
        return mariadb.connect(
            user=DB_USER, password=DB_PASS, host=DB_URL, port=3306, database="hackaton"
        )

    def update_query(self, query: str):
        self.__cursor.execute(query)
        self.__connection.commit()

    def get_query(self, query: str):
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def close(self):
        self.__connection.close()
