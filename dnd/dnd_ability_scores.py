import random
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

def setup_hero_stat_array(hero):
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

    # Loop through and assign 
    for key,value in hero.stats["ability_scores"].items():
        index = inquirer.select(
            message=f"Please assign a value for {key}",
            choices=list(map(lambda x: Choice(value=array.index(x), name=str(x)), array)),
        ).execute()
        value["sources"].append({"source": "Base Stat Array","val": array[index]})
        del array[index]
    return

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