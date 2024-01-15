from abc import ABC


class Engine(ABC):
    """Interface for engines"""

    def needs_service(self):
        """Returns True if the engine needs service"""
        pass
