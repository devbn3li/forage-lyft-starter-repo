import unittest

from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    """Tests for CapuletEngine"""

    def test_needs_service_true(self):
        """Test that needs_service returns True when the engine needs service"""
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        """Test that needs_service returns False when the engine doesn't need service"""
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
