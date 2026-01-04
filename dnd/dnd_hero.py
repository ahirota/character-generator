import json, os
from dnd.stats import setup_hero_stat_array
from dnd.dnd_class import setup_hero_class
from dnd.dnd_consts import Abilities

class DndHero():
    # Initialize Empty Stats for Hero
    def __init__(self, name):
        self.name = name
        self.dnd_class = {}
        self.stats = self.generate_baseline_stats()
        self.saving_throws = {
            
        }
        self.proficiencies = {
            "armor":[],
            "weapons":[],
            "tools":[],
            "languages":[]
        }
        self.origin = {}
        self.skills = self.generate_baseline_skills()
        self.feats = []
        self.equipment = []
    
    # Helper Function for initializing empty array
    def generate_baseline_stats(self):
        baseline_stats = {
            "hit_points": 0,
            "armor_class": 0,
            "initiative": 0,
            "ability_scores": {},
        }
        for ability in Abilities:
            baseline_stats["ability_scores"].update({ability.name: {"total": 0, "bonus": 0, "sources":[]}})
        self.stats = baseline_stats

    def generate_baseline_skills(self):
        baseline_skills = []
        filepath = os.path.abspath("data/dnd/skills.json")
        with open(filepath, "r") as file:
            skill_list = json.load(file)
        for skill in skill_list:
            baseline_skills.append({skill.name: {"mod": skill.attribute, "bonus": 0, "proficient": False}})
        self.skills = baseline_skills
    
    def get_stats(self):
        return self.stats
      
    def calculate_bonuses(self):
        return  

def make_new_hero(name):
    hero = DndHero(name)
    setup_hero_class(hero)
    setup_hero_stat_array(hero)
    return hero