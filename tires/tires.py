from abc import ABC


class Tires(ABC):
    """Interface for tires"""

    def needs_service(self):
        """Returns True if the tires need service"""
        pass
