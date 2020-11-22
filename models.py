# Paul Ho

class User:

    totalUsers = 0

    def __int__(self, name, email):
        # constructor
        self._name = name
        self._email = email
        User.totalUsers += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise TypeError("Please enter a valid name")
        else:
            self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if len(value) == 0:
            raise TypeError("Please enter a valid email")
        else:
            self._email = value

    def delete_user(self, email):
        pass

    def __str__(self):
        info = "Name: " + self._name, " Email: " + self._email
        return info
