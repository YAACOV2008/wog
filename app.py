from time import sleep

import currency_roulette_game
import guess_game
import memory_game
from score import add_score
from utils import screen_cleaner


def validation(typed_input):
    try:
        typed_input = int(typed_input)
        return True
    except ValueError:
        print(f"'{typed_input}' is not a number.")
        sleep(1)
        return False


def welcome():
    """This function prints the Welcome screen.
             :param username:
             :type wog_ascii_art: str
             :type username: str
             :return: None
             :rtype:
             """
    username = input("What is you name?")
    screen_cleaner()
    wog_ascii_art = f"""Hi {username} and welcome to the World of Games: The Epic Journey
    .------..------..------.
    |W.--. ||O.--. ||G.--. |
    | :/\: || :/\: || :/\: |
    | :\/: || :\/: || :\/: |
    | '--'W|| '--'O|| '--'G|
    `------'`------'`------'"""
    print(wog_ascii_art)


def start_play():
    """This function asks the user to select a game by entering the corresponding number.
    After choosing a game, the function will prompt the user to select a difficulty level between 1 and 5.
                 :param max_diff:
                 :type menu: int
                 :type max_diff: int
                 :type diff: int
                 :return: None
                 :rtype:
                 """
    max_diff = 5
    games_list = ("", memory_game, guess_game, currency_roulette_game)
    while True:
        menu = input("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second"
                     " and you have to guess it back.\n2. Guess Game - guess a number and see if you chose like the"
                     " computer.\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
                     "0. Exit\n------>")
        if validation(menu):
            menu = int(menu)
        else:
            continue
        if menu == 0:
            print("\nGoodbye!")
            sleep(1)
            break
        while True:
            diff = input(f"Please select a difficulty level between 1 to {max_diff}: ")
            if validation(diff):
                diff = int(diff)
                break
            else:
                continue
        if (1 <= menu <= 3) and (1 <= diff <= max_diff):
            if games_list[menu].play(diff):
                print("\nYou won! I wrote it in Scores.txt\n")
                add_score(diff)
                sleep(1)
                screen_cleaner()
            else:
                print("\nLOSER!!!\n Never mind, you will be better next time ;)\n")
                sleep(1)
                screen_cleaner()
        else:
            print("Wrong input, please try again")
            sleep(1)
