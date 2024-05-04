# T1A3-Terminal-App

## Links

### Trello Board
https://trello.com/invite/b/DYG0gN5B/ATTI96e347928dbf5aa7480f4c0f30fa08c9F3D43A87/python-apps

### GitHub
https://github.com/Noah-Morgan2/T1A3-Terminal-App


## Installation

### MacOS,Linux

1. Open a terminal 
2. Clone the Git Hub repository via SSH: ``git clone git@github.com:Noah-Morgan2/T1A3-Terminal-App.git``
    or via HTTPS:
   `` git clone https://github.com/Noah-Morgan2/T1A3-Terminal-App.git ``
3. Open src/ folder to gain access to apps via the terminal
    ``cd T1A3/src/``
4. In terminal type
    ``chmod +x run.sh``
    to execute permissions
5. To start app, type in terminal 
    ``.src/run.sh``
6. Congrats, you can now use my Contact Book

### Windows

1. Install WSL
2. Open a WSL terminal 
3. Clone GitHub repository via SSH:
    ``git clone git@github.com:Noah-Morgan2/T1A3-Terminal-App.git``
    or via HTTPS:
    `` git clone https://github.com/Noah-Morgan2/T1A3-Terminal-App.git ``
4. Open src/ folder to gain access to apps via the terminal
    ``cd T1A3/src/``
5. In terminal type
    ``chmod +x run.sh``
    to execute permissions
6. To start app, type in terminal 
    ``.src/run.sh``
7. Congrats, you can now use my Contact Book

## Prerequisites
- Python 
- Bash 
- Git

## Dependancies

This terminal app uses the following python libraries:

[Emoji](https://github.com/carpedm20/emoji?tab=readme-ov-file): A library of emojis for python. Is used to create a personal touch to the application

[Colored](https://pypi.org/project/colored/): A simple python library for color, is used to brighten up the terminal application.

# How To use
Below will be instructions on how to use the contact book. these instruction will be for after the app has been installed (via above) and the app is present in the terminal.

Starting with #1 Add New Contacts:

After selecting 1. user will be prompted with ``Add Contacts Name`` `` Add Contacts Phone Number`` `` Add Contacts Email`` `` Add Contacts Address`` You will be required to enter in each field with the intended contacts info. if you wish to leave a field blank press ``ENTER``. If done correctly you will be propted with ``Contact Added Successfully`` and taken back to the main menu.

#2 Search Contacts

After selecting #2 the user will be prompted with ``Enter Contacts Name``. After the user inputs the contacts name, the app will list all contacts with that name one after the other. Each Contact will list their Name, Phone Number, Email and Address if the user has filled in those fields, if not, next to each field will be blank. the user also get looped back to the main menu after all contacts have been displayed.

#3 View Contacts

After Selecting #3 the terminal will display all saved contacts(unlike #2 where it only displays one name). The user will not be prompted with anything and be looped back to the main menu.

#4 Edit Contacts

After Selecting #4 the user will be able to edit their contacts. First they will be prompted with `` Select A Contact To Edit
