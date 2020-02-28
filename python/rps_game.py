import random
import sys


def rps_game():

    wins = 0
    losses = 0
    ties = 0
    while True:
        print("-----------------------------")
        print("Wins: " + str(wins) + " - " + "Losses: " + str(losses) + " - " + "Ties: " + str(ties))
        print("-----------------------------")
        while True:
            print("Rock, Paper or Scissors? Enter either 'r', 'p' or 's' to play, or 'q' to quit: ")
            player_move = input()
            if player_move == "q":
                sys.exit()
            elif player_move == "r" or player_move == "p" or player_move == "s":
                break
        computer_moves = ["r", "p", "s"]
        computer_move = random.choice(computer_moves)

        if player_move == "r" and computer_move == "r":
            print("ROCK versus ROCK! It's a tie!")
            ties += 1
        elif player_move == "r" and computer_move == "p":
            print("ROCK versus PAPER! You lose!")
            losses += 1
        elif player_move == "r" and computer_move == "s":
            print("ROCK versus SCISSORS! You win!")
            wins += 1

        elif player_move == "p" and computer_move == "r":
            print("PAPER versus ROCK! You win!")
            wins += 1
        elif player_move == "p" and computer_move == "p":
            print("PAPER versus PAPER! It's a tie!")
            ties += 1
        elif player_move == "p" and computer_move == "s":
            print("PAPER versus SCISSORS! You lose!")
            losses += 1

        elif player_move == "s" and computer_move == "r":
            print("SCISSORS versus ROCK! You lose!")
            losses += 1
        elif player_move == "s" and computer_move == "p":
            print("SCISSORS versus PAPER! You win!")
            wins += 1
        elif player_move == "s" and computer_move == "s":
            print("SCISSORS versus SCISSORS! It's a tie!")
            ties += 1


print(rps_game())
