import random
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from dnd.dnd_consts import Abilities

def set_hero_ability_scores(**kwargs):
    # Initialize Ability Score Dict
    ability_scores = {}
    for stat in Abilities:
        ability_scores[stat.value] = 0
        
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

        print(f"\nYour {"Standard Array" if choice else "Random Array"} is as follows:")
        print(f"{ability_score_array}\n")

        choice = inquirer.select(
            message="How would you like to set your Ability Scores?",
            choices=[
                Choice(value=0, name="I'll manually set them."),
                Choice(value=1, name="Set them randomly with respect to my class."),
                Choice(value=2, name="Set them completely randomly."),
            ],
        ).execute()

        # Set Scores Manually
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
            if (choice == 1): kwargs["smart_flag"] = True
            ability_scores = set_random_scores(ability_scores, ability_score_array, **kwargs)
    else:
        ability_score_array = random.choice([get_standard_array(), get_rolled_array()])
        ability_scores = set_random_scores(ability_scores, ability_score_array, **kwargs)

    return ability_scores

def set_random_scores(ability_score_dict, ability_score_array, **kwargs):
    if (kwargs["smart_flag"]):
        random.shuffle(kwargs["stat_filter"])
        for stat in kwargs["stat_filter"]:
            ability_score_dict[stat] = max(ability_score_array)
            ability_score_array.remove(max(ability_score_array))

    for key in ability_score_dict:
        if (ability_score_dict[key] is not 0):
            continue
        ability_score_dict[key] = random.choice(ability_score_array)
        ability_score_array.remove(ability_score_dict[key])

    return ability_score_dict

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