class Preferences(object):

    # initialising variables from object creation

    def __init__(self, userID):
        self.userID = userID
        self.bedrooms = None
        self.maxPrice = None
        self.minPrice = None
        self.allergies = None
        self.residential = None
        self.transportPriority = None

    # creating set functions to set each value in the class and allow other classes to change parameters in these classes

    def setBedrooms(self, bedrooms):
        self.bedrooms = bedrooms

    def getBedrooms(self):
        return self.bedrooms

    def setMaxPrice(self, maxPrice):
        self.maxPrice = maxPrice

    def getMaxPrice(self):
        return self.maxPrice

    def setAllergies(self, allergies):
        self.allergies = allergies

    def getAllergies(self):
        return self.allergies

    def setTransportPriority(self, transportPriority):
        self.transportPriority = transportPriority

    def getTransportPriority(self):
        return self.transportPriority

    def setMinPrice(self, minPrice):
        self.minPrice = minPrice

    def setResidential(self, residential):
        self.residential = residential

    def getResidential(self):
        return self.residential

    # returning a preference object to be stored within the user class
    def loadPreferences(self, databaseValues):
        # this will load a preference and set all the internal values to those values which hasn't been implemented
        self.userID, self.bedrooms, self.maxPrice, self.minPrice, self.residential, self.transportPriority, self.allergies = databaseValues

    # saves the values to the database, hasn't been implemented
    def savePreferences(self):
        pass