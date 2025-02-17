import random
from time import sleep
from xml.dom import NotFoundErr

import requests


# Function to get live currency data for USD
def get_money_interval(difficulty):
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        currency = data["rates"]["ILS"]
        return currency, (10 - difficulty)
    else:
        return NotFoundErr


def get_guess_from_user():
    random_usd = random.randint(1, 100)
    while True:
        guess = input(f"""⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡾⠧⠀⠀⠥⢀⡀⠀⠀
⠀⠀⠀⢀⣴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠑⡄
⠀⠀⢠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠁
⠀⢀⣻⠁⠀⠀⠀⣰⢿⠀⠸⣽⣗⠖⠃⠀
⠀⠸⢼⠀⠀⠀⠀⣗⢽⠀⠄⠀⠁⠀⠀⠀
⠀⢸⠝⡆⠀⠀⠀⠈⠛⠃⠰⠤⢀⠀⠀⠀
⠀⠀⢯⠜⠦⡀⠀⠀⠀⠀⠀⠀⠀⠉⢂⠀
⠀⠀⠀⠓⢎⣝⠕⣲⡆⠀⡀⠀⠀⠀⠀⠆
⠀⠀⠀⠀⣄⠈⢙⢕⡇⠀⣿⡆⠀⠀⠀⢸
⠀⣠⠔⠉⠈⠑⠴⢬⡇⠀⡷⠃⠀⠀⠀⡈
⠸⡡⢓⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁
⠀⠈⠫⣎⡝⡢⢤⣀⠀⠀⣀⣀⡤⡾⠃⠀
⠀⠀⠀⠀⠉⠚⣔⣿⣤⣤⡽⠓⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠛⠛⠋⠀⠀⠀⠀⠀⠀
    ,How much is {random_usd} USD worth in Shekels?""")
        try:
            guess = int(guess)
        except ValueError:
            print(f"'{guess}' is not a number.")
            sleep(1)
            continue
        return random_usd, guess


def compare_results(get_guess, difficulty):
    currency_interval = get_money_interval(difficulty)
    currency_rate = float(currency_interval[0])
    interval = int(currency_interval[1])
    converted = int(currency_rate*int(get_guess[0]))
    print(f"\nThe converted value is: {converted}")
    return (converted - interval) <= int(get_guess[1]) <= (converted + interval)


def play(difficulty):
    return compare_results(get_guess_from_user(), difficulty)
