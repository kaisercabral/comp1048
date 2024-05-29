#
# File: Dice.py
# Description: This class is responsible to run the entire assessment code
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
#
import random


class Dice:
    """Store attributes of Dice - thrown strenght"""

    def __init__(self):
        """Define a 6 sided dice"""

        self.sides = 6

    def roll_dice(self, strength: int):
        """Roll the dice according to the strength set (1 - 5)"""

        number = random.randint(1, self.sides)
        if number + strength == self.sides:
            result = number + strength
        else:
            result = (number + strength) % self.sides

        return result

