class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, department, courseNum, quarter, year, instructor, review):
        """
        Inserts entry into database
        :param department: String
        :param courseNum: Int
        :param quarter: String
        :param year: Int
        :param instructor: String
        :param review: String
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass
       
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
        pass
