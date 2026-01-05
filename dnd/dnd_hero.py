from dnd.dnd_class import setup_hero_class
from dnd.dnd_origin import setup_hero_class
from dnd.dnd_ability_scores import setup_hero_stat_array


class DndHero():
    # Initialize Empty Hero Class Object
    def __init__(self, name):
        self.name = name
        self.dnd_class = {}
        self.origin = {}
        self.ability_scores = {}
        self.alignment = tuple()

    # Short Hand description with only Name, Ancestry, and Class
    def short_representation(self):
        return f"{self.name} - {self.origin["ancestry"]["name"]} {self.dnd_class["name"]}"

    # Guide User through Picking Parameters
    def guided_generate_self(self):
        pass

    # Generate random parameters
    # Smart build flag will use weights to skew choices towards synergistic options
    def random_generate_self(self, smart_build_flag = False):
        pass

    # Describes Character based on properties
    def self_one_liner(self):
        pass