from tires.tires import Tires


class OctoprimeTires(Tires):
    """Tires for an Octoprime"""

    def __init__(self, tire_wear):
        """Initializes an OctoprimeTires"""
        self.tire_wear = tire_wear

    def needs_service(self):
        """Returns True if the tires need service"""
        return sum(self.tire_wear) >= 3.0
