import random
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from dnd.dnd_consts import ALIGNMENTS, MORAL_WEIGHTS

def select_hero_alignment(**kwargs):
    if (kwargs["guided"]):
        choice = inquirer.select(
            message="How would you like to choose your Alignment?",
            choices=[
                Choice(value=0, name="I'll pick."),
                Choice(value=1, name="Give me a random choice that matches my class"),
                Choice(value=2, name="Completely Random."),
            ],
        ).execute()

        if (choice == 0):
            e_choices = list(map(lambda x: Choice(value=x, name=x.lower()), ALIGNMENTS["ETHICAL"]))
            ethical = inquirer.select(
                message="Please choose an ethical alignment.",
                choices=e_choices,
            ).execute()
            m_choices = list(map(lambda x: Choice(value=x, name=x.lower() if x is not "NEUTRAL" else f"{x.lower()} (This will result in True Neutral)"), ALIGNMENTS["MORAL"]))
            moral = inquirer.select(
                message="Please choose a moral alignment.\n(Please note that it is generally socially unacceptable to play an 'Evil' character.\nConsult your play group if you wish to select that alignment.",
                choices=m_choices,
            ).execute()

            alignment = tuple(ethical, moral)
        else:
            if (choice == 1): kwargs["smart_flag"] = True
            alignment = get_random_alignment(**kwargs)
    else:
        alignment = get_random_alignment(**kwargs)
    return alignment

def get_random_alignment(**kwargs):
    ethical = random.choice(ALIGNMENTS["ETHICAL"])
    moral = random.choices(ALIGNMENTS["MORAL"], weights=MORAL_WEIGHTS)[0] if (kwargs["smart_flag"]) else random.choice(ALIGNMENTS["MORAL"])
    return tuple(ethical, moral) 