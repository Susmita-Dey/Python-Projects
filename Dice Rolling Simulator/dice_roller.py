# import random
# define a function to roll the dice
# create a dictionary that will have drawing of the dice

import random


def roll_dice():
    dice_drawing = {
        1: (
            "---------",
            "|   1   |",
            "|   o   |",
            "|       |",
            "---------",
        ),
        2: (
            "---------",
            "| o     |",
            "|   2   |",
            "|     o |",
            "---------",
        ),
        3: (
            "---------",
            "| o 3   |",
            "|   o   |",
            "|     o |",
            "---------",
        ),
        4: (
            "---------",
            "| o   o |",
            "|   4   |",
            "| o   o |",
            "---------",
        ),
        5: (
            "---------",
            "| o 5 o |",
            "|   o   |",
            "| o   o |",
            "---------",
        ),
        6: (
            "--------",
            "| o   o |",
            "| o 6 o |",
            "| o   o |",
            "--------",
        ),

    }

    roll = input("Roll the dice? (Yes/No): ")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("Roll again? (Yes/No): ")


roll_dice()
