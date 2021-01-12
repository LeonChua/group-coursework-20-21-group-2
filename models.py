# Paul Ho
# This is a comment

class User(object):

    totalUsers = 0

    def __init__(self, name, email, university, password):
        # constructor
        self._name = name
        self._email = email
        self._university = university
        self._password = password
        User.totalUsers += 1
        self._userId = User.totalUsers

    #getName
    @property
    def name(self):
        return self._name
        """return the name stored in the User Object"""
        #pass
    #setName(String)
    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise TypeError("Please enter a valid name")
        else:
            self._name = value
        """set the name defined in value, if the is no input, raise an error"""
        #pass

    #getEmail
    @property
    def email(self):
        # return self._email
        """return the email stored in the User Object"""
        pass
    #setEmail(String)
    @email.setter
    def email(self, value):
        # if len(value) == 0:
            # raise TypeError("Please enter a valid email")
        # else:
            # self._email = value
        """set the email defined in value, if the is no input and no @ symbol, raise an error"""
        pass

    #getUniversity
    @property
    def university(self):
        """return the university stored in the User Object"""
        pass
    #setUniversity(String)
    @university.setter
    def university(self, value):
        """set the email defined in value, if the is no input, raise an error"""
        pass


    #getPassword
    @property
    def password(self):
        """return the password stored in the User Object"""
        pass
    #setPassword(String)
    @password.setter
    def university(self, value):
        """set the password defined in value, if the is no input, raise an error"""
        pass
    #getID
    @property
    def userId(self):
        """return the password stored in the User Object"""
        pass


    def __str__(self):
        info = "Name: " + self._name, " Email: " + self._email, " University: " + self._university, " ID: " + self._userId
        return info


#Mazin Abdulmahmood - Search Class
class search(object):
    #fff
    def getResult(self, data, index):
        '''Returns the data from a search result from a
        specific index. If the index is invalid raise
        exception.'''
        if index not in data:
            raise Exception("Index not in range")
        
        return data[index]

    def option_map(self, option):
        '''Maps the input option to the column the data is 
        found in the database.'''

        #Column representatons
        column_order = {
            "greenspaces":3,
            "safety":4,
            "crowdedness":5,
            "happiness":6,
            "traffic flow":7
        }

        if option not in column_order:
            raise Exception("Invalid filter option")

        return column_order[option]

    def filterSearch(self, data, option):
        '''Filter search result given option
        return index of highest option'''
        column_index = search.option_map(self, option)
        old = data[1][column_index]
        row_count = 1

        
        for i in range(2, len(data)):
            if data[i][column_index] > old:
                row_count += 1
                old = data[i][column_index]

        return row_count