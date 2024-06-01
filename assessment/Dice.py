#
# File: Dice.py
# Description: This class is responsible for keeping the attributes and functions of the entity dice
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
#
import random


class Dice:
    # Store attributes of Dice - thrown strength

    def __init__(self):
        # Define a 6 sided dice
        self.sides = 6

    def roll_dice(self, strength: int):
        # Roll the dice according to the strength set (0 - 5)
        number = random.randint(1, self.sides)
        if number + strength == self.sides:
            result = number + strength
        else:
            result = (number + strength) % self.sides
        return result

    def get_dice_faces(self, result):
        faces = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        return faces[result]



