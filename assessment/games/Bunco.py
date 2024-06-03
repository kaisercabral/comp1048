#
# File: Bunco.py
# Description: This class is responsible for the bunco games
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
#
from prettytable import PrettyTable
from assessment.games.Game import Game


class Bunco(Game):
    NAME = "Bunco"

    def __init__(self, players, num_rounds=1):
        super().__init__(2, 4, 3)
        self.players = players
        self.num_rounds = num_rounds
        self.scores = {player: 0 for player in players}
        self.round_points = {player: [0] * num_rounds for player in players}  # Initialize with 0 for all rounds
        self.buncos = {player: 0 for player in players}  # Record number of Buncos
        self.round_winners = []
        self.round = 1
        self.starting_player_index = 0  # Record the index of the starting player
        self.bets = {player: 0 for player in players}  # Record players bets

    def print_table(self):
        top_table = ['Round']
        row_total = ['Total']
        row_buncos = ['Bunco']
        for i in self.players:
            top_table.append(i.get_name())
            row_total.append(self.scores[i])
            row_buncos.append(self.buncos[i])

        table = PrettyTable(top_table)
        for round_num in range(self.num_rounds):
            row = [round_num + 1]
            for player in self.players:
                row.append(self.round_points[player][round_num])
            table.add_row(row)
        table.add_row(row_total)
        table.add_row(row_buncos)
        print(table)
        print("\n")

    def play_round(self):
        no_winner = True
        round_scores = {player: 0 for player in self.players}  # Initialize round scores for players
        while no_winner:
            for i in range(len(self.players)):
                player_index = (self.starting_player_index + i) % len(self.players)
                player = self.players[player_index]
                print(f"It's {player.get_name()}'s turn.")
                while round_scores[player] < 21:
                    rolls = []
                    strength = self.strength_msg()
                    for index, dice in enumerate(self.get_games_dices()):
                        result = dice.roll_dice(strength)
                        print(dice.get_dice_faces(result - 1), end=" ")
                        rolls.append(result)
                    print()

                    rounds_points = 0

                    if rolls.count(self.round) == 3:
                        if rolls[0] == self.round:
                            # Bunco
                            rounds_points = 21
                            # Record number of buncos
                            self.buncos[player] += 1
                            print("Bunco!\n")
                        else:
                            # Three of a kind of another number
                            rounds_points = 5
                    else:
                        rounds_points += rolls.count(self.round) * 2

                    round_scores[player] += rounds_points
                    self.scores[player] += rounds_points

                    msg = f"{player.get_name()} earned {rounds_points} points, {round_scores[player]} points in total."

                    if rolls.count(self.round) == 0:
                        print(f"\n{player.get_name()} earned no points, {round_scores[player]} points in total.")
                        break

                    print(msg)

                # Update the specific round score for the player
                self.round_points[player][self.round - 1] = round_scores[player]

                if round_scores[player] >= 21:
                    print(f"{player.get_name()} is the winner of round {self.round}\n")
                    no_winner = False
                    break
                else:
                    if rolls.count(self.round) > 0:
                        print(f"Keep playing {player.get_name()}")

    def play(self, players):
        print("Let the game begin!")
        # Play for num_rounds rounds
        for x in range(self.num_rounds):
            if self.round == 1:
                # Place Bets
                for i in players:
                    print(f"{i.get_name()} Place your bet!!!")
                    self.bets[i] = self.bet_msg(i)
            print(f"< Round {self.round} >")
            self.play_round()
            self.round += 1
            # Update the starting player index
            self.starting_player_index = (self.starting_player_index + 1) % len(self.players)

        self.print_table()

        overall_winner = max(self.scores, key=self.scores.get)

        # Print round points and Buncos for each player
        for player in self.players:
            if overall_winner.get_name() == player.get_name():
                rounds_won = sum(1 for scores in self.round_points.values() if scores[-1] == max(scores))
                print(f"{player.get_name()} won {rounds_won} rounds, scoring {self.scores[player]} points, with {self.buncos[player]} Buncos.")
                self.congratulations_msg(player, self.bets[player], False)
            else:
                self.sorry_msg(player, self.bets[player], False)
