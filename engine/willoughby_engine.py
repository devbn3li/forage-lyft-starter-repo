from engine.engine import Engine


class WilloughbyEngine(Engine):
    """A Willoughby engine"""
    def __init__(self, current_mileage, last_service_mileage):
        """Initializes a WilloughbyEngine"""
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        """Returns True if the engine needs service"""
        return self.current_mileage - self.last_service_mileage > 60000
