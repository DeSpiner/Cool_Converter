import time
import os
from values_to_convert import *

# This is to prevent future bugs
# if user uses Back function a lot of times
last_mode = None

# Creating an animation to the text
class Animated:

    def __init__(self, text, sleep_time):
        self.sleep_time = sleep_time
        self.text = text

    def show(self):
        for char in self.text:
            print(char, end="", flush=True)
            time.sleep(self.sleep_time)

# Function for showing all options
def main_menu():
    clear_terminal()

    Animated("You are on: Main Menu!", 0.02).show()
    time.sleep(0.3)

# Animated texts to navigate
    Animated("\nAvailable Choices:\n", 0.02).show()
    Animated("1. Convert - Views -=> Money\n", 0.02).show()
    Animated("2. Convert - Money -=> In-game currencies\n", 0.02).show()
    Animated("3. Convert - Text / Nums -=> binary\n", 0.02).show()
    Animated("4. Convert - ScreenTime -=> Things you could've made\n", 0.02).show()
    Animated("Your choice: (1-4): ", 0.02).show()

# Printing to the terminal

    choice = get_input()
    
    if choice is None:
        return

    global last_mode
    last_mode = choice

    match choice:
        case '1':
            views_to_money()
        case '2':
            in_game_currencies()
        case '3':
            binary_func()
        case '4':
            screen_time()

# Function for B keybind, goes back to the last opened tab in the program
def go_back():
    global last_mode

    if last_mode is None:
        main_menu()
        return

    match last_mode:
        case '1':
            views_to_money()
        case '2':
            in_game_currencies()
        case '3':
            binary_func()
        case '4':
            screen_time()

# Clearing the terminal
def clear_terminal():
    text = Animated("\nClearing the terminal...\n", 0.01) 
    text.show()
    for i in range(0, 101):
        print(f"\rLoading {i}% done...", end='', flush=True)
        time.sleep(0.01)
    os.system('cls')

# Showing the info about the program if user input = 'I'
def show_info():
    clear_terminal()
    Animated("You are on INFO tab\n\n", 0.02).show()
    print("")
    print("About this converter and its purpose.\n"
        "Was built by Maks in 8 days\n"
        "Its purpose: Quickly count money, currencies\n"
        "Convert all what author things is cool.\n\n"
        "KEYBINDS:\n"
        "Enter Q - Quit\n"
        "Enter I - Info\n"
        "Enter M - Menu\n"
        "Enter B - Back (to the last tab you have opened)\n\n"
        "Author: Maks.\n\n")
    print("Enter a Key-Bind:\t")

    choice = get_input()
    if choice is None: #This will be used a lot in a program for error handling
        return

# Making keybinds so that if any input is Q - leave, I - info ...
def get_input():
    value = input()
    value_clean = value.strip().upper()
    if value_clean == 'Q':
        Animated("Bye :(", 0.02).show()
        quit()
    elif value_clean == 'I':
        show_info()
        return None
    elif value_clean == 'M':
        main_menu()
        return None
    elif value_clean == 'B':
        go_back()
        return None
    return value

# COnverter for social meadias (Views on Social media -> money)
def views_to_money(): # Choice 1
    clear_terminal()
    main_text = ("Views On SocialMedia -> Money Converter!\n")
    Animated(f"You are on: {main_text}", 0.02).show()

# Condition 1
# Text for the SocialMedia Platform choice
    Animated("Choose the platform you want to work with:\n1. - Youtube\n2. - Instagram\n3. - Tiktok\nYour Choice:\t", 0.02).show()
    
    choice_1 = get_input()

    print("")

# Matching the SocialMedia Platform choice
    match choice_1:
        case '1':
            platform = "Youtube"
        case '2':
            platform = "Instagram"
        case '3':
            platform = "Tiktok"

# Condition 2
# Choosing type of the video
    if platform == "Youtube":
        Animated("Choose the type of the videos:\n1. - Long Form Video\n2. - Shorts (Short form video)\nYour Choice:\t", 0.02).show()
    elif platform == "Instagram":
        Animated("Choose the type of the videos:\n1. - Regular Video\n2. - Reels\n3. - Stories\nYour Choice:\t", 0.02).show()
    elif platform == "Tiktok":
        Animated("Chosen type of the video: Tiktok,\n press any key to continue\t", 0.02).show()
    
    choice_2 = get_input()
    print("")
# Matching the type of the video
    if platform == "Youtube" and choice_2 == '1':
        type_of_video = 'Long-Form Video'
    elif platform == "Youtube" and choice_2 == '2':
        type_of_video = 'Shorts'

    if platform == "Instagram" and choice_2 == '1':
        type_of_video = 'Regular Video'
    elif platform == "Instagram" and choice_2 == '2':
        type_of_video = 'Reels'
    elif platform == "Instagram" and choice_2 == '3':
        type_of_video = 'Stories'

    if platform == "Tiktok":
        type_of_video = 'Tiktok'

# Condition 3
# Choosing the currency
    Animated("Choose the currency:\n1. - Dollars\n2. - Euros\n3. - Hryvnia\nYour choice:\t", 0.02).show()
    choice_3 = get_input()
    print("")

    match choice_3:
        case '1':
            currency = 'Dollars'
        case '2':
            currency = 'Euros'
        case '3':
            currency = "Hryvnia's"

# Condition 4
# Choosing the operation
    Animated("Choose the operation:\n1. - Convert Views -->> Money.\n2. - Convert Money -->> Views.\nYour Choice:\t", 0.02).show()
    choice_4 = get_input()
    print("")

    match choice_4:
        case '1':
            convert = 'Views -->> Money'
        case '2':
            convert = 'Money -->> Views'

# Defining the CPM for each category (CPM - Cost Per Mile ($$$ for 1000 views))
    
    if platform == "Youtube" and type_of_video == "Long-Form Video":
        CPM = 2.5
    elif platform == "Youtube" and type_of_video == "Shorts":
        CPM = 0.8
    elif platform == "Instagram" and type_of_video == "Reels":
        CPM = 1.2
    elif platform == "Instagram" and type_of_video == "Regular Video":
        CPM = 1.5
    elif platform == "Instagram" and type_of_video == "Stories":
        CPM = 0.6
    elif platform == "Tiktok" and type_of_video == "Tiktok":
        CPM = 0.7
    else:
        print("Error. CPM is not defined.")
        CPM = 0

# Choosing the operation
    if convert == "Views -->> Money":
        try:
            views = int(input("Enter number of views: "))
            money_usd = (views / 1000) * CPM
        
        except ValueError:
            print("Please enter a valid integer")
# Preventing bugs if user input != int
    elif convert == "Money -->> Views":
        try:
            money_usd = float(input("Enter the amount of money in $: "))
            views = (money_usd / CPM) * 1000
        
        except ValueError:
            print("Please enter a valid integer")

# Converting the currency
    if currency == "Dollars":
        result = money_usd
    elif currency == "Euros":
        result = money_usd * 0.93
    elif currency == "Hryvnia's":
        result = money_usd * 38

# Printing the results
    if convert == 'Views -->> Money':
        Animated("\n\nConverting Views -->> Money\n", 0.02).show()
        Animated(f"Platform: {platform}\n", 0.02).show()
        Animated(f"Video Type: {type_of_video}\n", 0.02).show()
        Animated(f"Views: {views:.0f}\n", 0.02).show()
        Animated(f"Earnings: {result:.2f}{currency}", 0.02).show()

    elif convert == "Money -->> Views":
        Animated("\n\nConverting Money -->> Views\n", 0.02).show()
        Animated(f"Platform: {platform}\n", 0.02).show()
        Animated(f"Video Type: {type_of_video}\n", 0.02).show()
        Animated(f"Money: {money_usd:.2f}$\n", 0.02).show()
        Animated(f"Views: {views:.0f}\n\n", 0.02).show()
    
    print("")
    Animated("B - Back.  M - Menu.\nQ - Quit.  I - Info\nYour choice:\t", 0.02).show()
    inp = get_input()

    if inp is None:
        return

# Converter to in-game currencies
def in_game_currencies(): # Choice 2
    clear_terminal()
    main_text = ("Money -> InGame-Currencies Converter!\n")
    Animated(f"You are on: {main_text}\n", 0.02).show()
    Animated("Type the amount of money to convert(in USD):\nYour amount:\t", 0.02).show()
    amount_of_money = float(get_input())

    # Choosing the game
    Animated("Choose the game!:\n1. - Fortnite\n2. - Brawl Stars", 0.02).show()
    Animated("\n3. - Clash Of Clans\n4. - Hill climb 2\n5. - World Of Tanks\nYour Choice:\t", 0.02).show()
    game_choice = get_input()

    # Matching the choices
    match game_choice:
        case '1':
            game = 'Fortnite'
            in_game_curr = 'V-Bucks'
            result = amount_of_money / 0.01
            Animated(f"\n\nAmount of money: {amount_of_money}$\n", 0.02).show()
            Animated(f"Selected game: {game}\n", 0.02).show()
            Animated(f"In-game currency: {in_game_curr}\n", 0.02).show()
            Animated(f"Result: {amount_of_money}$ = {result:.2f} {in_game_curr}", 0.02).show()
        
        case '2':
            game = 'Brawl Stars'
            Animated('\nChoose the in-game currency:\n1. - Gems\n2. - Coins\nYour choice:\t', 0.02).show()
            choice2 = get_input()
            
            if choice2 == '1':
                in_game_curr = 'Gems'
                result = amount_of_money / 0.06

            elif choice2 == '2':
                in_game_curr = 'Coins'
                result = amount_of_money / 0.005 

            Animated(f"\n\nAmount of money: {amount_of_money}$\n", 0.02).show()
            Animated(f"Selected game: {game}\n", 0.02).show()
            Animated(f"In-game currency: {in_game_curr}\n", 0.02).show()
            Animated(f"Result: {amount_of_money}$ = {result:.2f} {in_game_curr}", 0.02).show()

        case '3':
            game = 'Clash Of Clans'
            Animated('\nChoose the in-game currency:\n1. - Gems\n2. - Coins\n3. - Elixir\n4. - Dark Elixir\nYour choice:\t', 0.02).show()
            choice3 = get_input()

            if choice3 == '1':
                in_game_curr = 'Gems'
                result = amount_of_money / 0.0045
            
            elif choice3 == '2':
                in_game_curr = 'Coins'
                result = amount_of_money / 0.00000225
            
            elif choice3 == '3':
                in_game_curr = 'Elixir'
                result = amount_of_money / 0.00000225
            
            elif choice3 == '4':
                in_game_curr = 'Dark Elixir'
                result = amount_of_money / 0.000225

            Animated(f"\n\nAmount of money: {amount_of_money}$\n", 0.02).show()
            Animated(f"Selected game: {game}\n", 0.02).show()
            Animated(f"In-game currency: {in_game_curr}\n", 0.02).show()
            Animated(f"Result: {amount_of_money}$ = {result:.2f} {in_game_curr}", 0.02).show()
        
        case '4':
            game = 'Hill Climb 2'
            Animated(
                '\nChoose the in-game currency:\n1. - Adventure Tokens\n2. - Gems\n3. - Coins\nYour choice:\t',0.02).show()
            choice4 = get_input()

            if choice4 == '1':
                in_game_curr = 'Adventure Tokens'
                result = amount_of_money / 0.00279

            elif choice4 == '2':
                in_game_curr = 'Gems'
                result = amount_of_money / 0.00155

            elif choice4 == '3':
                in_game_curr = 'Coins'
                result = amount_of_money / 0.00001033

            Animated(f"\n\nAmount of money: {amount_of_money}$\n", 0.02).show()
            Animated(f"Selected game: {game}\n", 0.02).show()
            Animated(f"In-game currency: {in_game_curr}\n", 0.02).show()
            Animated(f"Result: {amount_of_money}$ = {result:.2f} {in_game_curr}", 0.02).show()

        case '5':
            game = 'World Of Tanks'
            in_game_curr = 'Gold'
            result = amount_of_money * 225
            Animated(f"\n\nAmount of money: {amount_of_money}$\n", 0.02).show()
            Animated(f"Selected game: {game}\n", 0.02).show()
            Animated(f"In-game currency: {in_game_curr}\n", 0.02).show()
            Animated(f"Result: {amount_of_money}$ = {result:.2f} {in_game_curr}", 0.02).show()

        case _:
            print("Incorrect choice")
            return
        

# Showing the choices
    Animated("\n\nB - Back.  M - Menu.\nQ - Quit.  I - Info\nYour choice:\t", 0.02).show()
    inp = get_input()

    if inp is None:
        return

# Converter to and from binary
def binary_func():  # Choice 3
    clear_terminal()
    main_text = "Binary -> Text Converter!\n"
    Animated(f"You are on: {main_text}", 0.02).show()

    Animated("Choose the operation!\n1. - Binary -> Text\n2. - Text -> Binary\nYour choice:\t",0.02).show()
    print("")
    choice = get_input()

    match choice:
        case '1':
            operation = 'Binary -> Text'
        case '2':
            operation = 'Text -> Binary'
        case _:
            Animated("Wrong choice!\n", 0.02).show()
            return

    # Reverse dict
    binary_to_text = {v: k for k, v in binary.items()}

    if operation == 'Text -> Binary':
        Animated("Enter text:\t", 0.02).show()
        text = get_input()

        result = []
        for char in text:
            if char in binary:
                result.append(binary[char])
            else:
                result.append('?')

        Animated("Result:\n", 0.02).show()
        print(" ".join(result)) # Result is a list so we need to use .join

    elif operation == 'Binary -> Text':
        Animated("Enter binary (space separated):\t", 0.02).show()
        binary_input = get_input().split()

        result = []
        for byte in binary_input:
            if byte in binary_to_text:
                result.append(binary_to_text[byte])
            else:
                result.append('?')

        Animated("Result:\n", 0.02).show()
        print("".join(result))
    
    print("")
    Animated("B - Back.  M - Menu.\nQ - Quit.  I - Info\nYour choice:\t", 0.02).show()
    inp = get_input()

    if inp is None:
        return

# Convert screentime to things that could've been done
def screen_time(): #Choice 4
    clear_terminal()
    main_text = ("ScreenTime -> Things could've done Converter!\n")
    Animated(f"You are on: {main_text}\n", 0.02).show()
    Animated("How much screentime do you have?)\n", 0.02).show()
    Animated("Type it in and program will show you\nWhat you could've done instead!\nYour Screentime (in hours):\t", 0.025).show()
    value = get_input()
    
    # Preventing bugs
    if value is None:
        return
    
    # This code could make an error if user types not a int
    try:
        screen_time_input = int(value)
    except ValueError:
        Animated("Please enter a NUMBER.\n", 0.02).show()
        return
    
    # Print different messages based on the amount of screen time
    if screen_time_input <= 100:
        resp_text = f"Wow, you spent only {screen_time_input}hrs.. thats very low!"
    elif screen_time_input > 100 and screen_time_input < 500:
        resp_text = f"Yo {screen_time_input}hrs, you are avarage ._."
    elif screen_time_input >= 500 and screen_time_input < 1000:
        resp_text = f"Hear me out, but {screen_time_input}hrs is still low"
    elif screen_time_input >= 1000 and screen_time_input < 5000:
        resp_text = f"{screen_time_input}hrs... You need to touch some grass!"
    elif screen_time_input >= 5000:
        resp_text = f"At that point.. Just find a job, really."

    # Calculating the values to later use them
    books_red = screen_time_input / 3
    toilet_breaks = screen_time_input * 0.35
    battery_cycles = screen_time_input / 8
    new_languages = float(screen_time_input / 1000)
    fly_across_world = screen_time_input / 45
    # Printing the result of the calculations using f-strings
    Animated("\nIn time you wasted for internet:\n", 0.02)
    Animated(f"You had {battery_cycles:.0f} battery cycles\n", 0.02).show()
    Animated(f"Also had {toilet_breaks:.0f} toilet breaks\n", 0.02).show()
    Animated(f"Had opportunity to read {books_red:.0f} books\n", 0.02).show()
    Animated(f"Could've flown across the world {fly_across_world:.0f} times\n", 0.02).show()
    Animated(f"And also learn a new language {new_languages:.2f} times\n", 0.02).show()
    Animated(f"Cool right =) ?\n", 0.02).show()
    
    Animated("\nB - Back.  M - Menu.\nQ - Quit.  I - Info\nYour choice:\t", 0.02).show()
    inp = get_input()
    # Again to prevent bugs
    if inp is None:
        return

# To try things out
if __name__ == '__main__':
    pass #main()