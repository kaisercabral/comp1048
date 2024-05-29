#
# File: AllThatDice.py
# Description: This class is responsible for running the entire assessment code
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
#
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
        print("Welcome ", name + "!\n")
    else:
        # Check if name is alredy taken
        for player in players:
            if player.name.lower() == name.lower():
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
    list = sorted(players, key=lambda x: x.get_chips, reverse=True)
    for x in list:
        table.add_row([x.get_name(), x.get_games_played(), x.get_games_won(), x.get_chips()])
    print(table)
    print("\n")


# This function prints the games menu
def print_games_menu():
    return input(print("\nWhich games would you like to play?\n",
                       "(o) Odd-orEven\n",
                       "(m) Maxi\n",
                       "(b) Bunco\n>"))


class AllThatDice:

    def start_game(self):
        print("in")

    def end_game(self):
        print("in")

    def run(self):
        print("Welcome to All-That-Dice!\nDeveloped by Alan Turing\nCOMP 1048 Object-Oriented Programming\n\n")

        menu = "".join(["What would you like to do?\n",
                        "(r) register a new player\n",
                        "(s) show the leader board\n",
                        "(p) play a games\n",
                        "(q) quit\n>"])

        menu_option = input(menu)
        while not check_menu_option(menu_option):
            menu_option = input(menu)

        # Check if valid option
        if check_menu_option(menu_option):
            while menu_option != 'q':

                if menu_option == 'r':
                    name = input(print("What is the name of the new player?\n>"))
                    check_player(name)
                elif menu_option == 's':
                    if not players:
                        print("There's no players registered yet!\n")
                    else:
                        print_leader_board()
                elif menu_option == 'p':
                    game = print_games_menu()
                    while game not in ['o', 'm', 'b']:
                        print("Invalid option!")
                        game = print_games_menu()

                    if game == 'o':
                        
                        odd = OddOrEven(self)

                        # Check number of players
                        print("Passou")
                    # if not odd.check_number_of_players(len(players)):
                    #    odd.__del__()
                    # else:
                    #     """ Play Odd-Or-Even """
                    elif game == 'm':
                        # Check number of players
                        maxi = Maxi(players)
                        if not maxi.check_number_of_players(len(players)):
                            maxi.__del__()
                        else:
                            # Play Maxi
                            maxi.play()
                    else:
                        bunco = Bunco(players)
                        if not bunco.check_number_of_players(len(players)):
                            bunco.__del__()
                        else:
                            # Play Bunco
                            bunco.play()

                menu_option = input(print(menu))
                while not check_menu_option(menu_option):
                    menu_option = input(print(menu))

            print("Thank you for playing All-That-Dice")
            sys.exit()
