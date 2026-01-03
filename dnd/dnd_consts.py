from enum import Enum

STARTING_PROFICIENCY = 2
ARTISANS_TOOLS = ["CARPENTER","LEATHERWORKER","MASON","POTTER","SMITH","TINKER","WEAVER","WOODCARVER"]

class Abilities(Enum):
    STR = "strength"
    DEX = "dexterity"
    CON = "constitution"
    INT = "intelligence"
    WIS = "wisdom"
    CHA = "charisma"