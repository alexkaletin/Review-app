"""
Google datastore model
"""

from .Model import Model
from datetime import datetime
from google.cloud import datastore
from .translate import *

def from_datastore(entity):
        """
        Translate the top datastore result into a python list

        :return: a List
        """

        if not entity:
            return None
        if isinstance(entity, list):
            entity = entity.pop()
        return [entity['department'],entity['courseNum'],entity['quarter'],entity['year'],entity['instructor'],entity['review'],entity['translated']]

class model(Model):
    def __init__(self):
        #Creates client for querying the backend datastore service
        self.client = datastore.Client('cloud-f21-final')

    def select(self):
        """
        Returns reviews list of lists
        Each list in reviews contains: department, courseNum, quarter, year, instructor, review, translated
        :return: List of lists
        """ 
        """ kind = similar to table name
            entity = similar to row
        """

        query = self.client.query(kind = 'reviews')
        entities = list(map(from_datastore, query.fetch()))
        return entities
      
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
        """
        Firstly creates a new key called reviews
        then creates a new Entity using the key
        then updates object with correct information
        then puts via put() into datastore
        """

        # calls to translate review
        translated = translate_text(review, 'ru')

        key = self.client.key('reviews')
        rev = datastore.Entity(key)
        rev.update({
            'department': department,
            'courseNum': courseNum,
            'quarter': quarter,
            'year' : year,
            'instructor': instructor,
            'review': review,
            'translated': translated
            })
        self.client.put(rev)
        return True

    def delete(self, department, courseNum, quarter, year, instructor):
        """
        Delete entry from database
        :param department: String
        :param courseNum: Int
        :param quarter: String
        :param year: Int
        :param instructor: String
        :return: True
        """
        """ NOT DONE"""
        return True
