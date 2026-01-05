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

def select_hero_class(guided=True):
    # Load Class Data
    class_list = get_class_data()

    # Guided Class Selection
    if (guided):
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
            dnd_class = inquirer.select(
                message="Please choose a class",
                choices=list(map(lambda x: Choice(value=x, name=x.name), class_list)),
            ).execute()
        else:
            dnd_class = get_random_class(class_list)
    # Random Class Selection
    else:
        dnd_class = get_random_class(class_list)
    return dnd_class
    
def get_random_class(classes):
    return classes[random.randrange(len(classes))]