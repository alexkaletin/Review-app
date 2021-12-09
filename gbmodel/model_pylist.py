"""
Python list model
"""
from datetime import date
from .Model import Model
from .translate import *

class model(Model):
    def __init__(self):
        self.reviews = []

    def select(self):
        """
        Returns reviews list of lists
        Each list in reviews contains: department, courseNum, quarter, year, instructor, review
        :return: List of lists
        """
        return self.reviews

    def insert(self, department, courseNum, quarter, year, instructor, review):
        """
        Appends a new list of values representing new message into guestentries
        :param department: String
        :param courseNum: Int
        :param quarter: String
        :param year: Int
        :param instructor: String
        :param review: String
        :return: True
        """
        # calls to translate review
        translated = translate_text(review, 'ru')

        #formats parems and saves
        params = [name, department, courseNum, quarter, year, instructor, review, translated]
        self.reviews.append(params)
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
        
        return True
