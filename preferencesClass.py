class Preferences(object):

    # initialising variables from object creation

    def __init__(self, numberOfBedrooms, maxPrice, minPrice, allergies, connectedness):
        self.numberOfBedrooms = numberOfBedrooms
        self.maxPrice = maxPrice
        self.minPrice = minPrice
        self.allergies = allergies
        self.wellConnectedness = connectedness

    # creating set functions to set each value in the class and allow other classes to change parameters in these classes

    def setBedrooms(self, numberOfBedrooms):
        self.numberOfBedrooms = numberOfBedrooms

    def setMaxPrice(self, maxPrice):
        self.maxPrice = maxPrice

    def setAllergies(self, allergies):
        self.allergies = allergies

    def setWellconnectedness(self, connectedness):
        self.wellConnectedness = connectedness

    def setMinPrice(self, minPrice):
        self.minPrice = minPrice

    # returning a preference object to be stored within the user class
    def createPreferences(self):
        return self

