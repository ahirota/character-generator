import os, json, random

# To Do: Update KWARGs to Search for Parameters on Name generation
def generate_random_name(filename="data/names/fantasy_names.json", **kwargs):
    filepath = os.path.abspath(filename)
    with open(filepath, "r") as file:
        json_list = json.load(file)
    firsts = json_list["first_names"]
    lasts = json_list["last_names"]
    return f"{random.choice(firsts)} {random.choice(lasts)}"
