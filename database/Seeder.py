"""
Seeder class file
"""

import sqlite3 as sql


class Seeder:
    """
    Seeder class
    Contains methods used to seed database
    """

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn = sql.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def seed(self):
        """
        Seed database with dummy data
        """
        pass
