import unittest

from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    """Tests for SternmanEngine"""

    def test_needs_service_true(self):
        """Test that needs_service returns True when the engine needs service"""
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        """Test that needs_service returns False when the engine doesn't need service"""
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
