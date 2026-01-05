import os, json, random, sys
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

def setup_hero_class(hero, filename="data/dnd/classes.json", **kwargs):
    try:
        filepath = os.path.abspath(filename)
        with open(filepath, "r") as file:
            class_list = json.load(file)
    except Exception as e:
        print('An Error Ocurred when trying to load Class Data:')
        print(e)
        print('We\'re sorry, Exiting Application Now.')
        sys.exit(1)

    # Ask for Choice, Random Array or Standard Array
    choice = inquirer.select(
        message="Would you like to pick your class, or select one randomly?",
        choices=[
            Choice(value=True, name="I'll pick"),
            Choice(value=False, name="Random please"),
        ],
    ).execute()

    if choice:
        dnd_class = inquirer.select(
            message=f"Please pick a class",
            choices=list(map(lambda x: Choice(value=x, name=x.name), class_list)),
        ).execute()
    else:
        dnd_class = get_random_class(class_list)

    print("Your Class is:")
    print(dnd_class.name)
    
    
def get_random_class(classes):
    return classes[random.randrange(len(classes))]