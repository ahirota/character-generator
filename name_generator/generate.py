import os, json, random, sys

# To Do: Update KWARGs to Search for Parameters on Name generation
def generate_random_name(filename="data/names/fantasy_names.json", **kwargs):
    try:
        filepath = os.path.abspath(filename)
        with open(filepath, "r") as file:
            names_dict = json.load(file)
    except Exception as e:
        print('An Error Ocurred when trying to load Name Data:')
        print(e)
        print('We\'re sorry, Exiting Application Now.')
        sys.exit(1)
    firsts = names_dict["first_names"]
    lasts = names_dict["last_names"]
    return f"{random.choice(firsts)} {random.choice(lasts)}"
