from searchclass import search

class Testsearchclass:

    def test_getResults(self):
        data = {
            1:["Camden", "LocalPhotoURL", "MapCoordinates", "Statistic1", "Statistic2"],
            2:["Hackney", "LocalPhotoURL", "MapCoordinates", "Statistic1", "Statistic2"],
            3:["Islington", "LocalPhotoURL", "MapCoordinates", "Statistic1", "Statistic2"]
        }

        result = search.getResult(self, data, 2)

        assert result == ["Hackney", "LocalPhotoURL", "MapCoordinates", "Statistic1", "Statistic2"]

    def test_getResults2(self):
        data = {
            1:["Camden", "LocalPhotoURL", "MapCoordinates", "Statistic1", "Statistic2"],
            2:["Hackney", "LocalPhotoURL", "MapCoordinates", "Statistic1", "Statistic2"],
            3:["Islington", "LocalPhotoURL", "MapCoordinates", "Statistic1", "Statistic2"]
        }

        result = search.getResult(self, data, 4)

        assert result == False