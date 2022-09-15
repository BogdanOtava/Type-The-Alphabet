import pathlib
from string import ascii_lowercase
from time import sleep
from datetime import datetime

ALPHABET = ascii_lowercase
ROOT_PATH = pathlib.Path(__file__).parent
FILE_PATH = ROOT_PATH.joinpath("scores.txt")

def show_menu():
    """Returns the main menu for the game."""

    return(
        "-" * 30 + "\n" +
        "1. Play game" + "\n" +
        "2. See scoreboard" + "\n" +
        "3. Change username" + "\n" +
        "4. Exit menu" + "\n" +
        "-" * 30
        )

def start_countdown(seconds: int):
    """A simple function that will start a countdown.

    Args:
        * seconds -> (int): how many seconds should the countdown have.

    Raises:
        * ValueError: if the parameter is not an integer.
    """

    if seconds != int(seconds):
        raise ValueError("Seconds should be an integer.")

    while seconds > 0:
        print(seconds)
        seconds -= 1
        sleep(1)

print("Type the alphabet as fast as you can.")
print("Enter your username and press the number of the action you'd like to perform.\n")

user_name = input("Username: ")

while True:
    print(show_menu())

    user_choice = input(">>> ")

    if user_choice == "1":
        start_countdown(3)

        start = datetime.now()
        user_input = input(">>> ")
        stop = datetime.now()

        total_time = stop - start

        if user_input == ALPHABET:
            print(f"You typed the alphabet in {total_time.seconds}.{total_time.microseconds} seconds.")

            with open(FILE_PATH, "a") as scores:
                scores.write(f"{total_time.seconds}.{total_time.microseconds} - {user_name}\n")

        else:
            print("You typed something wrong.")

        sleep(1)

    elif user_choice == "2":
        with open(FILE_PATH, "r") as file:
            scoreboard = list(file)

            place = 0

            for scores in sorted(scoreboard):
                place += 1

                if place < 11:
                    print(f"{place}. {scores}")

        sleep(1)
        continue

    elif user_choice == "3":
        changed_user_name = input("Enter another username: ")
        user_name = changed_user_name

    else:
        break
