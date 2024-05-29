#
# File: Bunco.py
# Description: This class is responsible for the bunco game
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
#
from assessment.Game import Game

""" Play Bunco """

class Bunco(Game):
    rounds = 6

    def __init__(self, players):
        self.players = players

    def __del__(self):
        pass

