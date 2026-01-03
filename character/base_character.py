# Base Character Type
class BaseCharacter():
    def __init__(self, name=None, stats=None, gear=None, inventory=None):
        self.name = name
        self.stats = stats
        self.gear = gear
        self.inventory = inventory

    def __repr__(self):
        # must override
        pass