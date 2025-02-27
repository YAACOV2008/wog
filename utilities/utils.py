import click

SCORES_FILE_NAME = "../scores.txt"
BAD_RETURN_CODE = 404

def screen_cleaner():
    # Clear screen using click.clear() function
    click.clear()
    print("*** Screen Cleared ***")
    return
