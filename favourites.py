# Ben Li
# This is a new comment
# This is a new comment
class Favourites(object):

    def __init__(self, area_id, user_id, fav_list):
        self.area_id = area_id
        self.user_id = user_id
        self.fav_list = fav_list

    # adding a borough to the user's favourite list
    def insertEntry (self, area_id, fav_list):
        fav_list.add(area_id)
        return fav_list

    # removing a borough from the user's favourite list
    def removeEntry(self, area_id, fav_list):
        fav_list.remove(area_id)
        return fav_list

    # updating the overall Favourites table with all the favourites of all the users
    def updateFavourites(self,fav_list):
        Favourites.append(fav_list)
        return Favourites

    # returning the list of favourites to be stored in the user class
    def createFavourites(self):
        return self