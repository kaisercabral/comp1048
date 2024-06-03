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
    total = 0
    for y in dice:
        roll = y.roll_dice(strength)
        total = total + roll
        print(y.get_dice_faces(roll - 1), end=" ")
    return total


# method that prints the message when there's a draw
def print_draw_message(winners):
    print("\nPlayers remaining: ", end=" ")
    for index, x in enumerate(winners):
        if index < len(winners) - 1:
            print(x['player'], end=", ")
        else:
            print(x['player'])


# method that return the bet made by the player
def get_player_bet(player_name, results):
    for result in results:
        if result['player'] == player_name:
            return result['bet']
    return None


class Maxi(Game):
    NAME = "Maxi"

    def __init__(self, players):
        super().__init__(3, 5, 2)
        self.players = players
        self.initial_bets = {}

    # overriding abstract method
    def play(self, players):
        # Get the number of dices for the game
        dice = self.get_games_dices()
        print("Let the game begin!")
        winner = []
        results = []
        for index, player in enumerate(players):
            print(f"\nIt's {player.get_name()}'s turn.")
            bet = self.bet_msg(player)
            strength = self.strength_msg()
            sum_roll = roll_the_dice(dice, strength)

            results.append({
                "player": player.get_name(),
                "result": sum_roll,
                "index": index,
                "bet": bet
            })
        # find the highest result value
        highest_result = max(int(item['result']) for item in results)
        winners = check_winner(results)
        # flag to check when there's a winner
        no_winner = len(winners) > 1
        while no_winner:
            print_draw_message(winners)
            winners_result = []
            for x in winners:
                print(f"\nIt's {player.get_name()}'s turn.")
                strength = self.strength_msg()
                sum_roll = roll_the_dice(dice, strength)

                winners_result.append({
                    "player": x['player'],
                    "result": sum_roll,
                    "index": x['index'],
                    "bet": x['bet']
                })

            if len(winners) > 1:
                print_draw_message(winners)
            no_winner = (len(winners) > 1)
        winner = winners[0]

        print("\nCongratulations, {}! You win!".format(winner['player']), end=" ")

        # Add players number of games played and update chips
        for player_results in players:
            player_results.increase_games_played()
            bet = get_player_bet(player_results.get_name(), results)
            if player_results.get_name() == winner['player']:
                player_results.increase_games_won()
                player_results.add_chips(bet)
            else:
                player_results.subtract_chips(bet)

            print()
