import unittest

from favourites import Favourites


def favourite_list():
    favs = {'E09000007', 'E09000022', 'E09000023'}
    return favs

class TestFavourites(unittest.TestCase):

    def test_insertEntry(self,favs):

        Favourites.insertEntry(self, 'E09000003', favs)
        assert favs == {'E09000007', 'E09000022', 'E09000023', 'E09000003'}

    def test_removeEntry(self,favs):

        Favourites.removeEntry(self, 'E09000023', favs)
        assert favs == {'Camden', 'E09000022'}



