import sys

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.validator import EmptyInputValidator

from name_generator.generate import generate_random_name
from dnd.dnd_hero import DndHero

def main():
    # Start Character Generator
    print("Welcome to Character Generator. Let's make your next Character.")
    print("What kind of character would you like to make?")

    # Choose which kind of character you'd like to make. 
    # Currently only supports random fantasy names and DnD Heroes
    # To Do: Add support for other TTRPGs/Games
    generator_type = inquirer.select(
        message="What kind of character would you like to make?",
        choices=[
            Choice(value=0, name="I just want a random fantasy name."),
            Choice(value=1, name="A full Dungeons and Dragons Hero."),
        ],
    ).execute()

    # Generator type control block
    # Random Name Generator
    if (generator_type == 0):
        name = generate_random_name()
        print(f"Here's your random fantasy name:\n\n")
        separator = "+-" + "".join(["-" for char in range(len(name))]) + "-+"
        print(separator)
        print(f"| {name} |")
        print(separator)

    # DnD Character Generator Start
    elif (generator_type == 1):
        # Choose Random
        setup_flag = inquirer.select(
            message="Would you like to build your character from scratch?",
            choices=[
                Choice(value=0, name="Build from scratch."),
                Choice(value=1, name="Generate a random character."),
                Choice(value=2, name="Generate some options and I'll choose decide after."),
            ],
        ).execute()

        # Manual Setup Start
        if (setup_flag == 0):
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
            hero = DndHero(name)
            hero.populate_self(guided_flag=True, smart_flag=False)

        # Random Setup Start
        else:
            character_gen_count = 1

            # Multi-character generator override
            if (setup_flag == 2):
                character_gen_count = inquirer.number(
                    message="How many characters would you like to generate (maximum 10 characters)?",
                    min_allowed=1,
                    max_allowed=10,
                    validate=EmptyInputValidator(),
                ).execute()
                print(f"Generating {character_gen_count} character(s).")


            # Smart Flag Check, Will weight choices towards synergistic options
            smart_flag = inquirer.confirm(message=f"Do you want {'your character' if setup_flag == 1 else 'these characters'} built smartly?\nSmart characters will be weighted towards syngeristic options.", default=True).execute()
            
            # Save hero options
            hero_options = []
            chosen_hero_index = 0

            # Start Generator Loop
            for i in range(character_gen_count):
                name = generate_random_name()
                hero = DndHero(name)
                hero.populate_self(guided_flag=False, smart_flag=smart_flag)
                hero_options.append(hero)
            
            # Start Loop for choosing hero from options
            if (len(hero_options) > 1): 
                chosen = False
                hero_choices = list(map(lambda x: Choice(value=hero_options.index(x), name=x.short_representation()), hero_options))
                while not chosen:
                    index = inquirer.select(
                        message=f"Here's your options:",
                        choices=hero_choices,
                    ).execute()
                    print(f"Here's the details for {hero_options[index].name}:")
                    print(hero_options[index])
                    chosen = inquirer.confirm(message="Choose this character?", default=True).execute()
            
            hero = hero_options[chosen_hero_index]

        # Display Created/Chosen Hero Representation
        print("Here is you next DnD Hero")
        print("-------------------------\n\n")
        print(hero)

    # Invalid generator option 
    else:
        print("Something went wrong, invalid option chosen.")
        print("Exiting program")
        sys.exit(1)

    print("\n\n-------------------------")
    print("Thanks for using Character Generator!")

  
if __name__ == "__main__":
    main()