from dnd.stats import setup_hero_stat_array

class DndHero():
    def __init__(self, name):
        self.name = name
        self.stats = {}
        self.dnd_class = {}
        self.origin = {}
        self.skills = []
        self.feats = []
        self.equipment = []

    def calculate_bonuses(self):
        return
    
    def get_stats(self):
        return self.stats    

def make_new_hero(name):
    hero = DndHero(name)
    setup_hero_stat_array(hero)
    return hero