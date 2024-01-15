import unittest

from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    """Tests for WilloughbyEngine"""

    def test_needs_service_true(self):
        """Test that needs_service returns True when the engine needs service"""
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        """Test that needs_service returns False when the engine doesn't need service"""
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
