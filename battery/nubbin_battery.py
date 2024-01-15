from battery.battery import Battery
from utils import add_years_to_date


class NubbinBattery(Battery):
    """A battery that needs service every 3 years"""

    def __init__(self, current_date, last_service_date):
        """Initializes a NubbinBattery"""
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        """Returns True if the battery needs service"""
        date_which_battery_should_be_serviced_by = add_years_to_date(
            self.last_service_date, 4)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False
