from enum import Enum

class Abilities(Enum):
    STR = "STR"
    DEX = "DEX"
    CON = "CON"
    INT = "INT"
    WIS = "WIS"
    CHA = "CHA"

ALIGNMENTS = {
    "ETHICAL":["LAWFUL", "NEUTRAL", "CHAOTIC"],
    "MORAL":["GOOD", "NEUTRAL", "EVIL"]
}

MORAL_WEIGHTS = [20, 10, 1]