# Paul Ho

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
