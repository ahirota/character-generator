import random
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from dnd.dnd_consts import Abilities

def generate_hero_ability_scores(**kwargs):
    # Initialize Ability Score Dict
    ability_scores = {}
    for stat in Abilities:
        ability_scores[stat] = 0
        
    if (kwargs["guided"]):
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

        print(f"Your {"Standard Array" if choice else "Random Array"} is as follows:")
        print(ability_score_array)

        choice = inquirer.select(
            message="How would you like to set your Ability Scores?",
            choices=[
                Choice(value=0, name="I'll manually set them."),
                Choice(value=1, name="Set them randomly with respect to my class."),
                Choice(value=2, name="Completely Random."),
            ],
        ).execute()

        if (choice == 0):
            # Loop through and assign 
            for key in ability_scores:
                index = inquirer.select(
                    message=f"Please assign a value for {key}",
                    choices=list(map(lambda x: Choice(value=ability_score_array.index(x), name=str(x)), ability_score_array)),
                ).execute()
                ability_scores[key] = ability_score_array[index]
                del ability_score_array[index]
        else:
            if (choice == 1):
                for stat in random.shuffle(kwargs["stat_filter"]):
                    ability_scores[stat] = max(ability_score_array)
                    ability_score_array.remove(max(ability_score_array))

            for key in ability_scores:
                if (ability_scores[key] is not 0):
                    continue
                ability_scores[key] = random.choice(ability_score_array)
                ability_score_array.remove(ability_scores[key])

    else:
        ability_score_array = random.choice([get_standard_array(), get_rolled_array()])

        if (kwargs["smart_flag"]):
            for stat in random.shuffle(kwargs["stat_filter"]):
                ability_scores[stat] = max(ability_score_array)
                ability_score_array.remove(max(ability_score_array))

        for key in ability_scores:
            if (ability_scores[key] is not 0):
                continue
            ability_scores[key] = random.choice(ability_score_array)
            ability_score_array.remove(ability_scores[key])

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