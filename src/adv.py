from room import Room
from player import Player
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

print(room['outside'].name)

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
player = Player(input("Please enter your name: "), room['outside'])

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    print(player.player_location.name)
    print("")
    print(player.player_location.description)
    cmd = input("\n--> ")
    if cmd == 'q':
        print("Goodbye!")
        exit(0)
    elif cmd == "n":
        if player.player_location.n_to is not None:
            player.player_location = player.player_location.n_to
        else:
            print("You cannot move in that directon")
    elif cmd == "s":
        if player.player_location.s_to is not None:
                player.player_location = player.player_location.s_to
        else:
            print("you cannot move in that direction")
    elif cmd == "w":
        if player.player_location.w_to is not None:
                player.player_location = player.player_location.w_to
        else:
            print("you cannot move in that direction")
    elif cmd == "e":
        if player.player_location.e_to is not None:
                player.player_location = player.player_location.e_to
        else:
            print("you cannot move in that direction")

# def title_screen_selections():
#     option = input("> ")
#     if option.lower() == ('p'):
#         setup_game()
#     elif option.lower() == ('h'):
#         help_menu()
#     elif option.lower() == ('q'):
#         sys.exit()
#     while option.lower() not in ['p', 'h', 'q']:
#         print("Please enter a valid command.")
#         option = input("> ")
#         if option.lower() == ('p'):
#             setup_game()
#         elif option.lower() == ('h'):
#             help_menu()
#         elif option.lower() == ('q'):
#             sys.exit()

# def title_screen():
#     os.system('clear')
#     print('###############################')
#     print('#### WELCOME TO QUILT MAZE ####')
#     print('###############################')
#     print('Enter one:')
#     print('> [p]lay')
#     print('> [h]elp')
#     print('> [q]uit')
#     title_screen_selections()

# def help_menu():
#     print('#####################################')
#     print('############# HELP MENU #############')
#     print('#####################################')
#     print('Use [n]orth, [s]outh, [e]ast, [w]est to move.')
#     print('Enter p to play.')
#     print('Enter h for help menu.')
#     print('Enter q to quit.')
#     title_screen_selections()

# def setup_game():
#     ROOMNAME = '' 
#     DESCRIPTION = 'description'
#     EXAMINATION = 'examine'
#     SOLVED = False
#     NORTH = 'up', 'north'
#     SOUTH = 'down', 'south'
#     WEST = 'left', 'west'
#     EAST = 'right', 'east'

# zonemap = {
#     'outside': {

#     },
#     'store': {

#     },
#     'gallery': {

#     },
#     'sewing_room': {

#     },
#     'clearance': {

#     }
# }

