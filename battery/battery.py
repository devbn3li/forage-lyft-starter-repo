from abc import ABC


class Battery(ABC):
    """Interface for batteries"""

    def needs_service(self):
        """Returns True if the battery needs service"""
        pass
