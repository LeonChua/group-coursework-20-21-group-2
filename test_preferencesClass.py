import pytest
from preferencesClass import Preferences


@pytest.fixture(scope="function")
def preferences():
    yield Preferences(4, 1200, 600, True, 0.5)


class TestPreferences:
    # testing if setting values works by having only true tests
    def test_set_bedrooms(self, preferences):
        preferences.setBedrooms(5)
        assert preferences.numberOfBedrooms == 5

    def test_set_max_price(self, preferences):
        preferences.setMaxPrice(1500)
        assert preferences.maxPrice == 1500

    def test_set_allergies(self, preferences):
        preferences.setAllergies(False)
        assert preferences.allergies == False

    def test_set_wellconnectedness(self, preferences):
        preferences.setWellconnectedness(1)
        assert preferences.wellConnectedness == 1

    def test_set_min_price(self, preferences):
        preferences.setMinPrice(0)
        assert preferences.minPrice == 0

    # testing if it will return the same value as itself
    def test_create_preferences(self, preferences):
        assert preferences.createPreferences() == preferences
