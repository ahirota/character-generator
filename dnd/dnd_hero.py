from dnd.dnd_class import select_hero_class
from dnd.dnd_origin import select_hero_origin
from dnd.dnd_ability_scores import set_hero_ability_scores
from dnd.dnd_alignment import select_hero_alignment

class DndHero():
    # Initialize Empty Hero Class Object
    def __init__(self, name):
        self.name = name
        self.dnd_class = {}
        self.origin = {}
        self.ability_scores = {}
        self.alignment = tuple()

    def __repr__(self):
        name = self.name
        sep = ""

    # Short Hand description with only Name, Ancestry, and Class
    def short_representation(self):
        return f"{self.name} - {self.origin["ancestry"]["name"]} {self.dnd_class["name"]}"

    # Populate Self
    def populate_self(self, guided_flag=True, smart_flag=False):
        kwargs = {"guided":guided_flag, "smart_flag":smart_flag}
        self.dnd_class = select_hero_class(**kwargs)
        kwargs["stat_filter"] = self.dnd_class["primary_ability"]
        kwargs["class"] = self.dnd_class["class_name"]
        self.origin = select_hero_origin(**kwargs)
        self.ability_scores = set_hero_ability_scores(**kwargs)
        self.alignment = select_hero_alignment(**kwargs)

    # Describes Character based on properties
    def self_one_liner(self):
        pass

    # Don't forget to get your starting equipment etc...
    def character_continue_reminder_text(self):
        pass