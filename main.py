from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.validator import EmptyInputValidator
from character.name_generator.generate import generate_random_name

def main():
    # Start a Character Generator Loop

    # Say Hi, give options for what kind of character you want to build
    # Going to Start with just Dungeons and Dragons
    print("Welcome to Character Generator. Let's make your next Character.")
    print("----------------------------------------------------------")

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
    # Ask for Step by Step or just Random
    # If random, choose all and return with completed character Repr
    # Else, Go through Each Step and Allow User to Choose Things

    # Finally, Print Character to Screen
    #print(character)
    return
  
if __name__ == "__main__":
    main()