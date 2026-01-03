# Character Generator
Small Python Command-Line tool to generate and print out a character for various fantasy types.

Currently supported themes/games:
- Dungeons and Dragons

## Features
Uses the `InquirerPy` package to drive an interactive series of command-line prompts.

### Name Generator
Reads from a JSON File and randomly selects a first name and last name from the list. Additional parameters can be chosen to filter and narrow down a name.

### Dungeons and Dragons Specific Setup
Dungeons and Dragons (DnD) characters have a variety of parameters to set up and select. This tool guides you through that process, but can also randomly select from the available options (read via JSON Files). This setup follows the 2024 Player's Handbook Step by Step Guide and auto populates some things based on your choices.

These include:
- Class (and potentially Sub-class)
- Origin (Background, Equipment, Ancestry)
- Ability Scores
- Alignment
- Other Details

From your choices, the tool will provide you with a basic character sheet overview of your DnD Hero.

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
[ ] Finish DnD Generator
[ ] Add additional parameters for filtering and generating a name