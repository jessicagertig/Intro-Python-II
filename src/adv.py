from room import Room
import sys
import os

# Declare all the rooms

room = {
    'outside':  Room("Outside Sewing Store",
                     "North of you, the quilts in the store window beckon, sparking creativity."),

    'store':    Room("Sewing Store", """Dim light filters in from the south. Fabric and tools at high prices are displayed. Unlabeled doors can be seen to the north and east."""),

    'gallery': Room("Quilt Gallery", """A lighted hall stretchs into darkness, displaying beautiful quilts in fascinating patterns, unfortunately you can't afford the yardage to make a full quilt. A small window high in the wall shows a lighted room with a large red sign and the letters 'CLEARA...' beginning.  You can see no doors to that room."""),

    'sewing_room':   Room("Sewing Classroom", """The sewing room is a surprise behind the door on the west side of the store. Sewing machines and tools look ready for use.  and a curtained doorway is the northern corner"""),

    'clearance_fabric': Room("Clearance Fabric Room", """You've found the store's clearance fabric.  Sadly all the fabric looks incredibly ugly. The only exit is the curtained doorway on the south side of the room."""),
}


# _______
# |ga|cf| 
# |..|..|
# |st:sr|  
# |..|__|
# |ou|  
# |__|

# Link rooms together

room['outside'].n_to = room['store']
room['store'].s_to = room['outside']
room['store'].n_to = room['gallery']
room['store'].e_to = room['sewing_room']
room['gallery'].s_to = room['store']
room['sewing_room'].w_to = room['store']
room['sewing_room'].n_to = room['clearance_fabric']
room['clearance_fabric'].s_to = room['sewing_room']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def title_screen_selections():
    option = input("> ")
    if option.lower() == ('p'):
        setup_game()
    elif option.lower() == ('h'):
        help_menu()
    elif option.lower() == ('q'):
        sys.exit()
    while option.lower() not in ['p', 'h', 'q']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ('p'):
            setup_game()
        elif option.lower() == ('h'):
            help_menu()
        elif option.lower() == ('q'):
            sys.exit()

def title_screen():
    os.system('clear')
    print('###############################')
    print('#### WELCOME TO QUILT MAZE ####')
    print('###############################')
    print('Choose:')
    print('> [p]lay')
    print('> [h]elp')
    print('> [q]uit')
    title_screen_selections()

def help_menu():
    print('#####################################')
    print('############# HELP MENU #############')
    print('#####################################')
    print('Use north, south, east, west to move.')
    print('Enter p to play.')
    print('Enter h for help menu.')
    print('Enter q to quit.')
    title_screen_selections()

def setup_game():
    

