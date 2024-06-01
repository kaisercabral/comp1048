#
# File: AllThatDice.py
# Description: This class is responsible for running the entire assessment code
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
#
from __future__ import absolute_import

import sys
from prettytable import PrettyTable

from assessment.games import OddOrEven, Bunco, Maxi
from assessment.Player import Player

players = []


# This function checks if the input option is valid or not
def check_menu_option(option: str):
    if option not in ["r", "s", "p", "q"]:
        print("Option not valid!\n")
        return False
    else:
        return True


# This function checks if the name chosen is taken or not
def check_player(name: str):
    found = False
    if not players and isinstance(name, str):
        players.append(Player(name))
        print("Welcome", name + "!\n")
    else:
        # Check if name is alredy taken
        for player in players:
            if player.get_name().lower() == name.lower():
                print("Sorry, the name is already taken!\n")
                found = True
                break
        # If not taken, create new player with name provided and add them to the player's array
        if not found:
            players.append(Player(name))
            print("Welcome ", name + "!\n")


# This function prints the leader board
def print_leader_board():
    table = PrettyTable(['Name', 'Played', 'Won', 'Chips'])
    players_list = sorted(players, key=lambda x: x.get_chips(), reverse=True)
    for x in players_list:
        table.add_row([x.get_name(), x.get_games_played(), x.get_games_won(), x.get_chips()])
    print(table)
    print("\n")


# This function prints the games menu
def print_games_menu():
    return input(print("\nWhich games would you like to play?\n",
                       "(o) Odd-orEven\n",
                       "(m) Maxi\n",
                       "(b) Bunco\n",
                       "(x) Go Back\n"))


# This function searches for a player by their name and return their index
def return_player(name):
    for x in players:
        if x.get_name().lower() == name.lower():
            return x
    print("Player not found! Try again\n")


# This function prints the players menu
def print_players_menu(game):
    option = str.lower(game.NAME[0])
    if option == 'o':
        msg = "\nWho is playing {}?\n".format(game.NAME)
    else:
        msg = "\nHow many players? ( {} - {} )\n".format(game.get_min_players(), game.get_max_players())
    print(msg)


class AllThatDice:

    def run(self):
        print("Welcome to All-That-Dice!\nDeveloped by Arthur Cabral\nCOMP 1048 Object-Oriented Programming\n\n")

        menu = "".join(["What would you like to do?\n",
                        "(r) register a new player\n",
                        "(s) show the leader board\n",
                        "(p) play a game\n",
                        "(q) quit\n"])

        menu_option = input(menu)
        while check_menu_option(menu_option):
            if menu_option == 'q':
                print("Thank you for playing All-That-Dice")
                sys.exit()
            elif menu_option == 'r':
                name = input(print("What is the name of the new player?\n"))
                check_player(name)
            elif menu_option == 's':
                if not players:
                    print("There's no players registered yet!\n")
                else:
                    print_leader_board()
            elif menu_option == 'p':
                if not players:
                    print("There are no players registered.\n")
                else:
                    game = print_games_menu()
                    while game not in ['o', 'm', 'b', 'x']:
                        print("Invalid option!")
                        game = print_games_menu()
                    # if x, go back to the first menu
                    if game == 'x':
                        pass
                    if game == 'o':
                        odd = OddOrEven.OddOrEven()

                        # Print menu option
                        player_name = input(print_players_menu(odd))

                        # Search player
                        player = return_player(player_name)
                        while not player:
                            player = return_player(player_name)

                        # CHeck if player has enough chips to play
                        if player.get_chips() > 0:
                            odd.play(player)
                        else:
                            print("{} does not have enough chips to play!".format(player.get_name()))

                    elif game == 'm':
                        # Check number of players
                        maxi = Maxi.Maxi(players)
                        if not maxi.check_number_of_players(len(players)):
                            pass
                        else:
                            number_of_players = int(input(print_players_menu(maxi)))
                            while number_of_players < maxi.get_min_players() or number_of_players > maxi.get_max_players() :
                                print("Invalid number of players. Try again.")
                                number_of_players = int(input(print_players_menu(maxi)))

                            for i in range(1, number_of_players + 1):
                                # Search player
                                player = return_player(input(print(f"What is the name of player #{i}?")))
                                while not player:
                                    player = return_player(input(print(f"What is the name of player #{i}?")))

                                # if player not added yet, add to game's playing array
                                while not maxi.add_player(player):
                                    print(f"{player.get_name()} is already in the game!\n")
                                    # Search player
                                    player = return_player(input(print(f"What is the name of player #{i}?")))

                            maxi.play(maxi.get_playing())

                    elif game == 'b':
                        bunco = Bunco(players)
                        if not bunco.check_number_of_players(len(players)):
                            bunco.__del__()
                        else:
                            # Play Bunco
                            bunco.play()

            menu_option = input(menu)
