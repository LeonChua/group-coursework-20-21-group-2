class search(object):
    def getResult(self, data, index):
        if index not in data:
            return False
        else:
            return data[index]