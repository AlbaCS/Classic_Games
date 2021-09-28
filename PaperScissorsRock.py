# The purpose of this simple game is to show the power of conditional statements

import random

human_wins = 0
pc_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    value = input("Enter Paper, Scissors, or Rock to play, type Q to quit.").lower()
    if value == "q":
        if human_wins > pc_wins:
            print("Good Bye! You win:", human_wins)
            break
        elif human_wins < pc_wins:
            print("Good Bye! Computer Wins:", pc_wins)
            break
        else:
            print("TIE! You:", human_wins, "Computer:", pc_wins)
            break

    elif value not in options:
        print("Invalid Response, Try again!")

    else:
        random_number = random.randint(0, 2)
        c_guess = options[random_number]
        print("Computer:", c_guess + ".")

        if value == "paper" and c_guess == "scissors":
            print("Computer wins!")
            pc_wins += 1

        elif value == "scissors" and c_guess == "rock":
            print("Computer wins!")
            pc_wins += 1

        elif value == "rock" and c_guess == "paper":
                print("Computer wins!")
                pc_wins += 1

        else:
            print("You win!")
            human_wins += 1

# Random Generator
# Check Win
  # Check Tie
# Score Tracker
