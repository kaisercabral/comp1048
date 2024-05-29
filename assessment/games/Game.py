#
# File: Game.py
# Description: This class is the parent class for all the games available
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
#
from assessment import Player


class Game:
    name = None
    min_players = None
    max_players = None
    dices = None

    def __init__(self, players: Player):
        self.players = players

    def check_number_of_players(self, number_of_players: int):
        if number_of_players < self.min_players:
            print(f"Not enough players to play {self.name}\n")
            return False
        elif number_of_players > self.max_players:
            print(f"Too many players to play {self.name}\n")
            return False
        else:
            return True

    def play(self):
        raise NotImplementedError("Method should be implemented by subclasses")