from serviceable import Serviceable


class Car(Serviceable):
    """A car that needs service"""
    def __init__(self, engine, battery):
        """Initializes a car with an engine and battery"""
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        """Returns True if the car needs service"""
        return self.engine.needs_service() or self.battery.needs_service()
