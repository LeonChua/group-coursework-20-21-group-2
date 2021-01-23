import pytest
from preferencesClass import Preferences


@pytest.fixture(scope="function")
def preferences():
    yield Preferences(4)


class TestPreferences:
    # testing if setting values works by having only true tests
    def test_set_bedrooms(self, preferences):
        preferences.setBedrooms(5)
        assert preferences.bedrooms == 5

    def test_set_max_price(self, preferences):
        preferences.setMaxPrice(1500)
        assert preferences.maxPrice == 1500

    def test_set_allergies(self, preferences):
        preferences.setAllergies(False)
        assert preferences.allergies == False

    def test_set_transportPriority(self, preferences):
        preferences.setTransportPriority(1)
        assert preferences.transportPriority == 1

    def test_set_min_price(self, preferences):
        preferences.setMinPrice(0)
        assert preferences.minPrice == 0

    # testing if it will return the correct value
    def test_get_allergies(self, preferences):
        # need to set the value first
        preferences.allergies = False
        assert preferences.getAllergies() == False
