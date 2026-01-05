import random
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from dnd_consts import Abilities

def generate_hero_ability_scores():
    # Ask for Choice, Random Array or Standard Array
    choice = inquirer.select(
        message="Would you like to use the standard stat array, or generate one with the 4d6 drop lowest method?",
        choices=[
            Choice(value=True, name="Standard please"),
            Choice(value=False, name="Generate one for me please"),
        ],
    ).execute()

    # Get Stat Arrays
    if choice:
        ability_score_array = get_standard_array()
    else:
        ability_score_array = get_rolled_array()

    print("Your Stat Array is as follows:")
    print(ability_score_array)

    # Initialize Ability Score Dict
    ability_scores = {}
    for stat in Abilities:
        ability_scores[stat] = 0

    # Loop through and assign 
    for key in ability_scores:
        index = inquirer.select(
            message=f"Please assign a value for {key}",
            choices=list(map(lambda x: Choice(value=ability_score_array.index(x), name=str(x)), ability_score_array)),
        ).execute()
        ability_scores[key] = ability_score_array[index]
        del ability_score_array[index]

    return ability_scores

def get_standard_array():
    return [15, 14, 13, 12, 10, 8]

def get_rolled_array():
    stat_array = []
    for i in range(6):
        stat_array.append(four_d6_drop_lowest())
    return stat_array

def four_d6_drop_lowest():
    statrolls = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    statrolls.remove(min(statrolls))
    return sum(statrolls)