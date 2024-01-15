from tires.tires import Tires


class CarriganTires(Tires):
    """Tires for a Carrigan"""

    def __init__(self, tire_wear):
        """Initializes a CarriganTires"""
        self.tire_wear = tire_wear

    def needs_service(self):
        """Returns True if the tires need service"""
        for tire in self.tire_wear:
            if tire >= 0.9:
                return True
        return False
