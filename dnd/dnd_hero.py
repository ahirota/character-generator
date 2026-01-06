from prettytable import PrettyTable

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
        sep = "-------------"
        ancestry = f"{self.origin["ancestry"]["optional_type"]} " if "optional_type" in self.origin["ancestry"] else ""
        sub_line = f"{self.alignment_to_string()} {ancestry}{self.origin["ancestry"]["ancestry_name"]} {self.dnd_class["class_name"]}"
        ability_score_title = "Ability Scores"

        ability_scores = PrettyTable()
        for score,val in self.ability_scores.items():
            ability_scores.add_column(score, [val])

        background = f"Background: {self.origin["background"]["background_name"]} | Starting Feat: {self.origin["background"]["feat"]}"
        traits = f"Traits: {", ".join(self.origin["ancestry"]["traits"])}"

        return "\n".join([name,sep,sub_line,sep,ability_score_title,ability_scores.get_string(),background,traits])

    # Populate Self
    def populate_self(self, guided_flag=True, smart_flag=False):
        kwargs = {"guided":guided_flag, "smart_flag":smart_flag}
        self.dnd_class = select_hero_class(**kwargs)
        kwargs["stat_filter"] = self.dnd_class["primary_ability"]
        kwargs["class"] = self.dnd_class["class_name"]
        self.origin = select_hero_origin(**kwargs)
        self.ability_scores = set_hero_ability_scores(**kwargs)
        self.alignment = select_hero_alignment(**kwargs)

    # Short Hand description with only Name, Ancestry, and Class
    def short_representation(self):
        return f"{self.name} - {self.origin["ancestry"]["ancestry_name"]} {self.dnd_class["class_name"]}"
    
    # Self Alignment to String
    def alignment_to_string(self):
        return f"{self.alignment[0].capitalize() if self.alignment[0] != self.alignment[1] else "True"} {self.alignment[1].capitalize()}"

    # Don't forget to get your starting equipment etc...
    def character_continue_reminder_text(self):
        return """Hopefully this helps you get set up. Don't forget to choose your starting equipment, add your ability score bonuses, and choose any extra options your feats/origins give you. Good luck and Happy Playing!"""