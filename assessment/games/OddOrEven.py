#
# File: OddOrEven.py
# Description: This class is responsible for the odd or even games
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
#
from assessment.games.Game import Game


class OddOrEven(Game):
    NAME = "Odd Or Even"

    def __init__(self):
        super().__init__(1, 1, 1)

    def play(self, player):
        # Get the number of dices for the game
        dice = self.get_games_dices()

        # Player should choose
        choice = input(print(f"Hey {player.get_name()}, Odd (o) or Even (e)?"))
        while choice not in ["o", "e"]:
            print("Option not valid! Try again!")
            choice = input(print(f"Hey {player.get_name()}, Odd (o) or Even (e)?"))

        if player.get_chips() < 1:
            print("Not enough chips")
        else:
            # record the bet from the player
            bet = self.bet_msg(player)

            # record the strength the player is going to throw the dice
            strength = self.strength_msg()

            # increase games played
            player.increase_games_played()

            # print the dice faces
            for x in dice:
                roll = x.roll_dice(strength)
                print(x.get_dice_faces(roll - 1), end=" \n")

                # check if player won or lost
                if (roll % 2 == 0 and choice == 'e') or (roll % 2 == 1 and choice == 'o'):
                    self.congratulations_msg(player, bet, True)
                else:
                    self.sorry_msg(player, bet, True)