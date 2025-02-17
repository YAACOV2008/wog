from mimetypes import guess_type
import random
from time import sleep


def generate_number(difficulty):
    return random.randint(0, difficulty)


def get_guess_from_user(difficulty):
    while True:
        guess = input(f"""      _W_
    _ (")
     \/ /\_
      \ \ \
      
    __///__
   ,The computer guessed a number between 0 and {difficulty}.... Can you guess it?""")
        try:
            guess = int(guess)
        except ValueError:
            print(f"'{guess}' is not a number.")
            sleep(1)
            continue
        if (0 <= guess <= difficulty):
            return guess
        else:
            print("Wrong input, please try again")
            sleep(1)


def compare_results(secret, guess):
    return secret == guess


def play(difficulty):
    secret = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(secret, guess)
