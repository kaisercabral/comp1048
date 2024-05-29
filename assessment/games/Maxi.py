#
# File: Maxi.py
# Description: This class is responsible for the maxi game
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
#

from assessment.Game import Game


class Maxi(Game):

    def __init__(self, players):
        self.players = players

    def __del__(self):
        pass

    # overriding abstract method
    def play(self):
        number_of_players = int(input(print(f"Let's play the game of {self.GAME_NAME} !\n",
                                            f"How many players ({self.MIN_PLAYERS}-{self.MAX_PLAYERS})?")))

        playing = []

        for x in range(number_of_players):
            ok = False
            while not ok:
                player_name = input(print(f"What is the name of player #{x+1}?"))
                for y in self.players:
                    if player_name.lower() == y.name.lower():
                        playing.append(y)
                        ok = True
                        break
                if not ok:
                    print(f"There is no player called {player_name}.\n")

