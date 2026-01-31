# Importing all features
from conv_functions import *
from values_to_convert import *
import time
import os
# Clearing terminal for good looks
os.system('cls')

# Introducing user to the converter
Animated("Hello and Welcome to my project! ^-^\n", 0.02).show()
Animated("This is a not standart converter, with some\n", 0.02).show()
Animated("Cool features like text -> binary convert\n\n", 0.02).show()
time.sleep(0.3)

Animated("Here are some keybinds you would need:\n"
        "1. Enter Q - Quit the program\n"
        "2. Enter I - Opens up the Info\n"
        "3. Enter M - Opens up the Main Menu\n"
        "4. Enter B - Goes Back to the last converter you chose\n"
        , 0.02).show()

Animated("\nPress enter to confirm you have red the instruction!", 0.02).show()

# To confirm user red the instruction
confirm = get_input()

# Starting the program
if confirm.lower() != 'secret':
    main_menu()
else:
    clear_terminal()
    Animated("You Discovered a secret code!\n", 0.02).show()
    print("╔══════════════════════════════════════════════════════════╗")
    print("║ [ ⚠ ]  T O P   S E C R E T  //  C L A S S I F I E D [ ⚠ ]║")
    print("╚══════════════════════════════════════════════════════════╝")
    Animated("Now enjoy the rogram!", 0.02).show()
    time.sleep(3)
    main_menu()