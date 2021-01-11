import pytest
from models import search

@pytest.fixture
def input_data():
    data = {
            1:["Camden", "LocalPhotoURL", "MapCoordinates", "43", "78"],
            2:["Hackney", "LocalPhotoURL", "MapCoordinates", "12", "66"],
            3:["Islington", "LocalPhotoURL", "MapCoordinates", "34", "82"]
        }
    return data

class Testsearchclass:
    def test_getResults(self, input_data):
        #Test the indexing functionality of getResults
        result = search.getResult(self, input_data, 2)

        #Index 2 would represent the data for Hackney from the dictionary
        assert result == ["Hackney", "LocalPhotoURL", "MapCoordinates", "12", "66"]

    def test_getResults2(self):
        #Test out of range Exception that is raised by class if the index
        #is out of range

        with pytest.raises(Exception):
            result = search.getResult(self, input_data, 4)
    
    def test_filterSearch(self, input_data):
        #Test highest entry of chosen option to be filtered
        result = search.filterSearch(self, input_data, "greenspaces")

        assert result == 1

    def test_filterSearch2(self, input_data):
        #Test out of range error exception
        with pytest.raises(Exception):
            result = search.filterSearch(self, input_data, "pollution")
        