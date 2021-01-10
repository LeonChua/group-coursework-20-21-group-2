#Mazin Abdulmahmood - Search Class

class search(object):
    def getResult(self, data, index):
        #Returns the data from a search result from a
        #specific index. If the index is invalid return
        #False.

        if index not in data:
            return False
        else:
            return data[index]