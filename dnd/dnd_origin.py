import os, json, random, sys
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

DND_ANCESTRY_FILE_PATH = "data/dnd/ancestries.json"
DND_BACKGROUND_FILE_PATH = "data/dnd/backgrounds.json"

def get_origin_data(path):
    try:
        filepath = os.path.abspath(path)
        with open(filepath, "r") as file:
            origin_data = json.load(file)
    except Exception as e:
        print('An Error Ocurred when trying to load Class Data:')
        print(e)
        print('We\'re sorry, Exiting Application Now.')
        sys.exit(1)
    return origin_data

def select_hero_origin(guided=True, **kwargs):
    # Initialize Empty Hero Origin Object
    dnd_origin = {"background":{}, "ancestry":{}}

    # Load Background Data and Choose Background
    background_list = get_origin_data(DND_BACKGROUND_FILE_PATH)
    dnd_origin["background"] = select_hero_background(guided, background_list, **kwargs)

    # Load Ancestry Data and Choose Ancestry
    ancestry_list = get_origin_data(DND_ANCESTRY_FILE_PATH)
    dnd_origin["ancestry"] = select_hero_ancestry(guided, ancestry_list)

    return dnd_origin


def select_hero_background(guided, background_list, **kwargs):
    # Guided Background Selection
    if (guided):
        # Prompt User for choice
        choice = inquirer.select(
            message="Would you like to choose your background, or select one randomly?",
            choices=[
                Choice(value=0, name="I'll choose."),
                Choice(value=1, name="Give me a random choice that matches my class."),
                Choice(value=2, name="Give me totally random please."),
            ],
        ).execute()

        # Choose Background or Randomize
        if (choice == 0):
            verbose_flag = inquirer.confirm(message=f"Do you want a detailed overview of these options?", default=False).execute()
            if verbose_flag: print(f"You are a {kwargs["class"]} and your {"Primary Abilities are" if len(kwargs["stat_filter"]) > 1 else "Primary Ability is"} {kwargs["stat_filter"]}")
            background_choices = list(map(lambda x: Choice(value=x, name=f"{x["background_name"]}{f" with Feat: {x["feat"]}\nPairs well with characters that have these primary abilities: {x["primary_ability"]}" if verbose_flag else ""}"), background_list))
            dnd_background = inquirer.select(
                message="Please choose a background:",
                choices=background_choices,
            ).execute()
        else:
            if (choice == 1):
                kwargs["smart_flag"] = True
            dnd_background = get_random_background(background_list, **kwargs)
    # Random Background Selection
    else:
        dnd_background = get_random_background(background_list, **kwargs)
    return dnd_background

# Currently checks if ANY primary ability matches
# Should this check if ALL primary abilities match? How to weight between them?
def get_random_background(background_list, **kwargs):
    if ("smart_flag" in kwargs and kwargs["smart_flag"] == True):
        stat_filter = kwargs["stat_filter"]
        filtered_dict = {}
        for k,v in background_list.items():
            if any(x in v["primary_ability"] for x in stat_filter):
                filtered_dict[k] = background_list[k]
        background_list = filtered_dict
    return background_list[random.randrange(len(background_list))]


# Does not need kwargs for any smart filtering
def select_hero_ancestry(guided, ancestry_list):
    # Guided Ancestry Selection
    if (guided):
        # Prompt User for choice
        choice = inquirer.select(
            message="Would you like to choose your ancestry, or select one randomly?",
            choices=[
                Choice(value=0, name="I'll choose."),
                Choice(value=1, name="Give me a random choice."),
            ],
        ).execute()

        # Get Ancestry or Randomize
        if (choice == 0):
            ancestry_choices = list(map(lambda x: Choice(value=x, name=f"{x["ancestry_name"]} with Feat: {x["feat"]}\nPairs well with characters"), ancestry_list))
            
            dnd_ancestry = inquirer.select(
                message="Please choose an Ancestry",
                choices=ancestry_choices,
            ).execute()

            # If Subtype Found, Prompt User to Select One
            if dnd_ancestry["optional_type"] is not None:
                print("Your Ancestry has a special subtype.")
                dnd_ancestry_subtype = inquirer.select(
                    message="Please choose one:",
                    choices=dnd_ancestry["optional_type"],
                ).execute()
                dnd_ancestry["optional_type"] = dnd_ancestry_subtype
        else:
            dnd_ancestry = get_random_ancestry(ancestry_list)
            if dnd_ancestry["optional_type"] is not None:
                dnd_ancestry_subtype = dnd_ancestry["optional_type"][random.randrange(len(dnd_ancestry["optional_type"]))]
                dnd_ancestry["optional_type"] = dnd_ancestry_subtype
    # Random Ancestry Selection
    else:
        dnd_ancestry = get_random_ancestry(ancestry_list)
        if dnd_ancestry["optional_type"] is not None:
            dnd_ancestry_subtype = dnd_ancestry["optional_type"][random.randrange(len(dnd_ancestry["optional_type"]))]
            dnd_ancestry["optional_type"] = dnd_ancestry_subtype
    return dnd_ancestry

def get_random_ancestry(ancestry_list):
    return ancestry_list[random.randrange(len(ancestry_list))]

