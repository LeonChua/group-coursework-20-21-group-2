#Mazin Abdulmahmood - Search Class

class search(object):
    #Incomplete class, algorithm yet to be developed

    def getResult(self, data, index):
        #Returns the data from a search result from a
        #specific index. If the index is invalid raise
        #exception.
        if index not in data:
            raise Exception("Index not in range")
        
        return data[index]

    def option_map(self, option):
        #Maps the input option to the column the data is 
        #found in the database.

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
        column_index = search.option_map(self, option)
        old = data[1][column_index]
        row_count = 1

        for i in range(2, len(data)):
            if data[i][column_index] > old:
                row_count += 1
                old = data[i][column_index]

        return row_count