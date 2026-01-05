# Character Generator
Small Python Command-Line tool to generate a few options for your next character.

Currently supported themes/games:
- Dungeons and Dragons

## Features
Uses the `InquirerPy` package to drive an interactive series of command-line prompts.

### Name Generator
Reads from a JSON File and randomly selects a first name and last name from the list. Additional parameters can be chosen to filter and narrow down a name.

### Dungeons and Dragons Specific Setup
Utilizing JSON Files, the DnD Generator will output a few options for your next character with a few key details. Options for generating a "smart" base stat array are also available.

Character details will be formatted as below, and hopefully this can serve as a jumping off point for your next DnD Hero
`{NAME} | Level 1 {ANCESTRY_OPTION}{ANCESTRY} {CLASS}, with the {ORIGIN} Background.`
```
| Base Stats | STR | DEX | CON | INT | WIS | CHA |
|------------|-----|-----|-----|-----|-----|-----|
|            |     |     |     |     |     |     |
```

## Running this Project
To run this project, please follow the steps below. Make sure you have the prerequisites and then follow the step by step

### Pre-requisites
You'll need `uv` to run this project. You can get it here:

https://github.com/astral-sh/uv?tab=readme-ov-file#installation

### Installation
To set up and run this project, follow these steps:

1. Clone this repository:
2. Navigate to the project directory: 
3. Install Dependencies: `uv sync`
4. Run the script: `uv run main.py`

## Questions/Comments/Concerns?
Feel free to reach out to me:
- Email: avjhirota@gmail.com
- Discord: @neinhearted

## Road Map
- [ ] Refactor for Smaller Scope (Was a bit ambitious the first go around)
- [ ] Class Picker/Generator
- [ ] Origin Picker/Generator
- [ ] Feat Picker/Generator
- [ ] Add additional parameters for filtering and generating a name