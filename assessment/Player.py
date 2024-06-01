#
# File: Player.py
# Description: This class is responsible for recording the player's details
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
#


class Player:
    # Store attributes of player - name, chips, turn, games played and games won

    def __init__(self, name):
        # Construct an obejct of Player class
        self.set_name(name)
        self.set_chips(100)
        self.set_games_played(0)
        self.set_games_won(0)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_chips(self, chips):
        self._chips = chips

    def get_chips(self):
        return self._chips

    def set_games_played(self, games_played):
        self._games_played = games_played

    def get_games_played(self):
        return self._games_played

    def set_games_won(self, games_won):
        self._games_won = games_won

    def get_games_won(self):
        return self._games_won

    def __str__(self):
        return f"Player(name:{self._name}, games_played={self._games_played}, games_won={self._games_won}, chips={self._chips})"

    def add_chips(self, quantity: int):
        # Add chips to player when player's won a games
        self.set_chips(self.get_chips() + quantity)

    def subtract_chips(self, quantity: int):
        # Subtract chips from player when player's lost a games
        self.set_chips(self.get_chips() - quantity)

    def increase_games_played(self):
        # Increase number of games played when player finishes a games
        self.set_games_played(self.get_games_played() + 1)

    def increase_games_won(self):
        # Increase number of games won when player wins a games
        self.set_games_won(self.get_games_won() + 1)

    def check_bet_ammount(self, chips: int):
        # This function checks if the amount bet is lower than chips available
        return chips <= self.get_chips()