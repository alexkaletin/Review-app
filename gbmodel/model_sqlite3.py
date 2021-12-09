"""
A simple reviews flask app.
Data is stored in a SQLite database that looks something like the following:

+------------+------------------+------------+----------------+------+-----------+
| department | courseNum        | quarter  | year    | instructor    | review    |
+============+==================+============+----------------+------+-----------+
| CS         | 55555            | Fall     | 2021    |Feng           |Great inst |
+------------+------------------+------------+----------------+------+-----------+

This can be created with the following SQL (see bottom of this file):

    create table reviews (department text, courseNum int, quarter text, year int, instructor text, review text)";

"""
from .Model import Model
import sqlite3
from .translate import *
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from reviews")
        except sqlite3.OperationalError:
            cursor.execute("create table reviews (department text, courseNum int, quarter text, year int, instructor text, review text, translated text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: department, courseNum, quarter, year, instructor, review, translated
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reviews")
        return cursor.fetchall()

    def insert(self,  department, courseNum, quarter, year, instructor, review):
        """
        Inserts entry into database
        :param department: String
        :param courseNum: Int
        :param quarter: String
        :param year: Int
        :param instructor: String
        :param review: String
        :return: True
        :raises: Database errors on connection and insertion
        """

        # calls to translate review
        translated = translate_text(review, 'ru')

        params = {'department':department, 'courseNum':courseNum, 'quarter':quarter, 'year':year, 'instructor':instructor, 'review':review, 'translated':translated}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into reviews (department, courseNum, quarter, year, instructor, review, translated) VALUES (:department, :courseNum, :quarter, :year, :instructor, :review, :translated)", params)

        connection.commit()
        cursor.close()
        return True
        
    def delete(self, department, courseNum, quarter, year, instructor):
        """
        Delete entry from database
        :param department: String
        :param courseNum: Int
        :param quarter: String
        :param year: Int
        :param instructor: String
        :return: none
        """
        params = {'department':department, 'courseNum':courseNum, 'quarter':quarter, 'year':year, 'instructor':instructor}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM reviews WHERE department=:department AND courseNum=:courseNum AND quarter=:quarter AND year=:year AND instructor=:instructor", params)
        connection.commit()
        cursor.close()
        return True
