import random
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from dnd.dnd_consts import Abilities

def setup_hero_stat_array(hero):
    # Initialize Stats
    hero.stats = generate_baseline_stats()

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
        array = get_standard_array()
    else:
        array = get_rolled_array()

    print("Your Stat Array is as follows:")
    print(array)

    # If Stat Array is poorly rolled, ask for reroll
    # if sum(array) < 60:
    #     print("Looks Rough, do you want to reroll these?")
    #     move_on = False
    #     while not move_on:
    #         break

    for key,value in hero.stats["ability_scores"].items():
        index = inquirer.select(
            message=f"Please assign a value for {key}",
            choices=list(map(lambda x: Choice(value=array.index(x), name=str(x)), array)),
        ).execute()
        value["sources"].append({"source": "Base Stat Array","val": array[index]})
        del array[index]
    return


def generate_baseline_stats():
    baseline_stats = {
        "hit_points": 0,
        "armor_class": 0,
        "initiative": 0,
        "ability_scores": {},
    }
    for ability in Abilities:
        baseline_stats["ability_scores"].update({ability.name: {"total": 0, "bonus": 0, "sources":[]}})
    return baseline_stats 

def get_standard_array():
    return [15, 14, 13, 12, 10, 8]

def get_rolled_array():
    stat_array = []
    for i in range(6):
        stat_array.append(four_d6_drop_lowest())
    return stat_array

def four_d6_drop_lowest():
    statrolls = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    print(statrolls)
    statrolls.remove(min(statrolls))
    print(statrolls)
    return sum(statrolls)