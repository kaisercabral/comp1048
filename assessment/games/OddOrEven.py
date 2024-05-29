#
# File: OddOrEven.py
# Description: This class is responsible for the odd or even game
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
#
from assessment.Game import Game


class OddOrEven(Game):

    def __init__(self):
        self.min_players = 1
        self.max_players = 1
        self.dices = 1
        self.name = "Odd Or Even"

    def __del__(self):
        pass

    def print_odd(self):
        print("Odds")

    def play(self, Game):
        number_of_players = int(input(print(f"Let's play the game of {self.name} !\n",
                                            f"How many players ({self.min_players}-{self.max_players})?")))

        playing = []

        for x in range(number_of_players):
            ok = False
            while not ok:
                player_name = input(print(f"What is the name of player #{x + 1}?"))
                for y in self.players:
                    if player_name.lower() == y.name.lower():
                        playing.append(y)
                        bet = input(print(f"How many chips would you bid {player_name} (1-{y.chips})?"))

                        """ Check if chips are available. """
                        if y.check_bet_amount(bet):
                            print("Entrou")

                        ok = True
                        break
                if not ok:
                    print(f"There is no player called {player_name}.\n")