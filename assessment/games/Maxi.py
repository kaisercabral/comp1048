#
# File: Maxi.py
# Description: This class is responsible for the maxi games
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
#

from assessment.games.Game import Game


# method that checks if there's a winner
def check_winner(results):
    if not results:
        return []

    # find the highest result value
    highest_result = max(int(item['result']) for item in results)

    # filter the dictionaries that have the highest result value
    winners = [item for item in results if int(item['result']) == highest_result]

    return winners


# method that rolls the dice and return the sum of the roll
def roll_the_dice(dice, strength):
    sum = 0
    for y in dice:
        roll = y.roll_dice(strength)
        sum = sum + roll
        print(y.get_dice_faces(roll - 1), end=" ")
    return sum


# method that prints the message when there's a draw
def print_draw_message(winners):
    print("\nPlayers remaining: ", end=" ")
    for index, x in enumerate(winners):
        if index < len(winners) - 1:
            print(x['player'], end=", ")
        else:
            print(x['player'])


class Maxi(Game):
    NAME = "Maxi"

    def __init__(self, players):
        super().__init__(3, 5, 2)

    # overriding abstract method
    def play(self, players):
        # Get the number of dices for the game
        dice = self.get_games_dices()

        print("Let the game begin!")

        # flag to check when there's a winner
        no_winner = True
        while no_winner:
            # make a dictionary in order to record the results
            results = []
            for index, x in enumerate(players):
                print("\nIt's {}' turn.".format(x.get_name()))
                # record the bet from the player
                bet = self.bet_msg(x)

                # record strength of throw
                strength = self.strength_msg()

                # Roll the dice and record the sum of the roll
                sum = roll_the_dice(dice, strength)

                results.append({"player": x.get_name(), "result": int(sum), "index": int(index), "bet": int(bet)})

            winners = check_winner(results)
            while len(winners) > 1:
                results = []
                print_draw_message(winners)
                for x in winners:
                    print("\nIt's {}' turn.".format(x['player']))

                    # record the strength the player is going to throw the dice
                    strength = self.strength_msg()

                    # Roll the dice and record the sum of the roll
                    sum = roll_the_dice(dice, strength)

                    results.append({"player": x.get_name(), "result": int(sum), "index": int(index)})
                winners = check_winner(results)

            no_winner = False

            print("\nCongratulations, {}! You win!".format(winners[0]['player']), end=" ")

            # Add players number of games played
            for x in players:
                x.increase_games_played()
                # increase the winner games won
                if x.get_name() == winners[0]['player']:
                    x.increase_games_won()
                else:
                    # decrease chips
                    x.subtract_chips(bet)

            print()
