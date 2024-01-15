import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    """Tests the NubbinBattery class"""

    def test_needs_service_true(self):
        """Test that needs_service returns True when the battery needs service"""
        current_date = date.fromisoformat("2024-01-15")
        last_service_date = date.fromisoformat("2010-09-15")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        """Test that needs_service returns False when the battery doesn't need service"""
        current_date = date.fromisoformat("2022-02-25")
        last_service_date = date.fromisoformat("2016-01-11")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
