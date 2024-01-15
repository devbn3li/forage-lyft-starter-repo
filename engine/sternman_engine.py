from engine.engine import Engine


class SternmanEngine(Engine):
    """A Sternman engine"""

    def __init__(self, warning_light_is_on):
        """Initializes a SternmanEngine"""
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        """Returns True if the engine needs service"""
        if self.warning_light_is_on:
            return True
        else:
            return False
