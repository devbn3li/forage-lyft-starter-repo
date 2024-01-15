from abc import ABC, abstractmethod


class Serviceable(ABC):
    """Interface for serviceable objects"""
    @abstractmethod
    def needs_service(self):
        """Returns True if the object needs service"""
        pass
