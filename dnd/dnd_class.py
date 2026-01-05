import os, json, random, sys
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

DND_CLASS_FILE_PATH = "data/dnd/classes.json"

def get_class_data():
    try:
        filepath = os.path.abspath(DND_CLASS_FILE_PATH)
        with open(filepath, "r") as file:
            class_list = json.load(file)
    except Exception as e:
        print('An Error Ocurred when trying to load Class Data:')
        print(e)
        print('We\'re sorry, Exiting Application Now.')
        sys.exit(1)
    return class_list

def select_hero_class(**kwargs):
    # Load Class Data
    class_dict = get_class_data()

    # Guided Class Selection
    if (kwargs["guided"]):
        # Prompt User for choice
        choice = inquirer.select(
            message="Would you like to choose your class, or select one randomly?",
            choices=[
                Choice(value=True, name="I'll choose."),
                Choice(value=False, name="Random please."),
            ],
        ).execute()

        # Get Class or Randomize
        if choice:
            class_choices = []
            for k,v in class_dict.items():
                class_choices.append(Choice(value=k, name=v["class_name"]))
            key = inquirer.select(
                message="Please choose a class",
                choices=class_choices,
            ).execute()
            dnd_class = class_dict[key]
        else:
            dnd_class = get_random_class(class_dict)
    # Random Class Selection
    else:
        dnd_class = get_random_class(class_dict)
    return dnd_class
    
def get_random_class(class_dict):
    return class_dict[random.choice(list(class_dict))]