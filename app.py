from time import sleep


def welcome():
    """This function prints the Welcome screen.
             :param username:
             :type wog_ascii_art: str
             :type username: str
             :return: None
             :rtype:
             """
    username = input("What is you name?")
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
    while True:
        max_diff = 5
        menu = input("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second"
              " and you have to guess it back.\n2. Guess Game - guess a number and see if you chose like the"
              " computer.\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
              "------>")
        diff = input(f"Please select a difficulty level between 1 to {max_diff}: ")
        try:
            menu = int(menu)
            diff = int(diff)
        except ValueError:
            print(f"'{menu}' or '{diff}' are not numbers.")
            sleep(1)
            continue
        if (1 <= menu <= 3) and (1 <= diff <= max_diff):
            return
        else:
            print("Wrong input, please try again")
            sleep(1)



