import unittest
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestState(unittest.TestCase):
    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")
        self.assertTrue(hasattr(state, "name"))


class TestCity(unittest.TestCase):
    def test_attributes(self):
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))


class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertTrue(hasattr(amenity, "name"))


class TestPlace(unittest.TestCase):
    def test_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])


class TestReview(unittest.TestCase):
    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))


if __name__ == '__main__':
    unittest.main()
