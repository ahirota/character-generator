from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.validator import EmptyInputValidator
from name_generator.generate import generate_random_name
from dnd.dnd_hero import make_new_hero

def main():
    # Start a DnD Hero Generator
    print("Welcome to DnD Hero Generator. Let's make your next Hero.")
    print("----------------------------------------------------------")

    # Ask for Step by Step or just Random
    # If random, choose all and return with completed character Repr
    # Else, Go through Each Step and Allow User to Choose Things
    # rand_flag = inquirer.confirm(message="Do you want us to completely randomize your character?", default=False).execute()

    # Ask for a Name, or Randomly Generate One (use First - Last Style)
    name_select = inquirer.select(
        message="Do you have a name in mind? Or would you like us to generate one for you?",
        choices=[
            Choice(value=True, name="I have a name in mind."),
            Choice(value=False, name="Generate one for me please."),
        ],
    ).execute()

    if name_select:
        name = inquirer.text(
            message="What's your character's name?",
            validate=EmptyInputValidator("Your name cannot be empty"),
        ).execute()
    else:
        name = generate_random_name()

    print(f"Okay {name}, let's get you set up.")
  
    hero = make_new_hero(name)
    print(hero.get_stats())
    
    return
  
if __name__ == "__main__":
    main()