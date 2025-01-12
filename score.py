from time import sleep

from utils import SCORES_FILE_NAME


def add_score(difficulty):
    while True:
        try:
            score_file = open(SCORES_FILE_NAME, mode="r")
            score = (score_file.readlines())
            print(f"Your current score is: {score[0]}")
            score_file = open(SCORES_FILE_NAME, mode="w")
            new_score = int(score[0])+(difficulty * 3 + 5)
            print("Your\033[1m new\033[0m score is:" + '\033[1m'+str(new_score))
            score_file.write(str(new_score))
            break
        except FileNotFoundError:
            print("Score could not be read!")
            score_file = open(SCORES_FILE_NAME, mode="w")
            score_file.write("0")
        finally:
            sleep(1)
            score_file.close()
