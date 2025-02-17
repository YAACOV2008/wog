import random
from time import sleep

from utils import screen_cleaner


def generate_sequence(difficulty):
    rand_list = []
    for i in range(difficulty):
        rand_list.append(random.randint(1, 101))
    return rand_list


def get_list_from_user(rand_list):
    length_list = len(rand_list)
    print(f"Watch carefully and try to remember:\n{rand_list}")
    sleep(0.7)
    screen_cleaner()
    while True:
        user_list = input(f"""⠀⠀⠀⣀⣤⣶⡶⠿⢿⣿⣶⣶⣤⣀⠀⠀⠀
⠀⢀⣾⣿⠋⠁⠀⠀⠀⠀⠙⢿⣿⣿⣷⣄⠀
⠀⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⡄
⠘⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇
⠀⠹⢿⣿⠟⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⠟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡿⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀Do you remember what the {length_list} numbers were?\n
Enter elements separated by\033[1m space: """).split()
        if not all(n.isdigit() for n in user_list):
            screen_cleaner()
            print(user_list)
            print("Not all the elements entered are digits. Please try again.")
            continue
        # Iterating over list
        i: int
        for i in range(len(user_list)):
            # Converts each element to an integer
            user_list[i] = int(user_list[i])
        return user_list


def is_list_equal(rand_list):
    return get_list_from_user(rand_list) == rand_list


def play(difficulty):
    rand_list = generate_sequence(difficulty)
    return is_list_equal(rand_list)
