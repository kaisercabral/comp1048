#
# File: Game.py
# Description: This class is the parent class for all the games available
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
#
from assessment.Dice import Dice


class Game:

    def __init__(self, min_players, max_players, dice):
        self.set_min_players(min_players)
        self.set_max_players(max_players)
        self.set_dice(dice)
        self.set_playing([])

    def set_min_players(self, min_players):
        self._min_players = min_players

    def get_min_players(self):
        return self._min_players

    def set_max_players(self, max_players):
        self._max_players = max_players

    def get_max_players(self):
        return self._max_players

    def set_dice(self, dice):
        self._dice = dice

    def get_dice(self):
        return self._dice

    def get_games_dices(self):
        dice = []
        for x in range(self.get_dice()):
            dice.append(Dice())
        return dice

    def check_number_of_players(self, number_of_players: int):
        if number_of_players < self.get_min_players():
            print(f"Not enough players to play {self.NAME} ({self.get_min_players()} - {self.get_max_players()})\n")
            return False
        else:
            return True

    def strength_msg(self):
        strength = int(input(print("How strong will you throw (0-5)?\n")))
        while strength < 0 or strength > 5:
            print("Invalid input!")
            strength = int(input(print("How strong will you throw (0-5)?\n")))
        return strength

    def bet_msg(self, player):
        bet = int(input(print("How many chips would you bid? (1 - {})\n".format(player.get_chips()))))
        while not player.check_bet_ammount(bet):
            print("Invalid input!")
            bet = int(input(print("How many chips would you bid? (1 - {})\n".format(player.get_chips()))))
        return bet

    def sorry_msg(self, player, bet, show_message):
        # subtract the chips
        player.subtract_chips(bet)
        if show_message:
            print("Sorry, {}! You lose!".format(player.get_name()), end=" ")

    def congratulations_msg(self, player, bet, show_message):
        # Add the chips
        player.add_chips(bet)

        # increase games won
        player.increase_games_won()
        if show_message:
            print("Congratulations, {}! You win!".format(player.get_name()), end=" ")

    def set_playing(self, players):
        self._playing = players

    def get_playing(self):
        return self._playing

    def add_player(self, player):
        if not self.is_player_playing(player):
            self._playing.append(player)
            return True
        return False

    def is_player_playing(self, player):
        return self._playing.count(player) > 0

    def play(self):
        raise NotImplementedError("Method should be implemented by subclasses")

