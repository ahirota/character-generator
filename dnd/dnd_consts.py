from enum import Enum

STARTING_PROFICIENCY = 2

ARTISANS_TOOLS = ["CARPENTER","LEATHERWORKER","MASON","POTTER","SMITH","TINKER","WEAVER","WOODCARVER"]

class Abilities(Enum):
    STR = "STR"
    DEX = "DEX"
    CON = "CON"
    INT = "INT"
    WIS = "WIS"
    CHA = "CHA"