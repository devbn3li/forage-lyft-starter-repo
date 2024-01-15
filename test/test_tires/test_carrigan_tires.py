import unittest

from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    """Tests for CarriganTires"""

    def test_needs_service_true(self):
        """Test that needs_service returns True when the tires need service"""
        tire_wear = [0.1, 0.3, 0.2, 0.9]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        """Test that needs_service returns False when the tires don't need service"""
        tire_wear = [0.1, 0.2, 0.4, 0.2]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())
