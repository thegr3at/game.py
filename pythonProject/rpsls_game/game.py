# Author: Ahmed Fath Allah
# Date: 7/27/22
# Project: Creating rock, paper, and scissors game.

# importing the random module
import random

# welcoming the user to playing our game
print("Welcome to the Rock-Paper-Scissors-Lizard-Spock game")

# asking user to enter their name
name = input("Please enter your name to continue: ")

# printing the rules of the game
print(f"Welcome {name}, here are the rules to the game")
print(f"******************************"
      f"\nRule #1: scissors cuts paper. "
      f"\nRule #2: paper covers rock. "
      f"\nRule #3: rock crushes lizard. "
      f"\nRule #4: lizard poison spock. "
      f"\nRule #5: spock smashes scissors. "
      f"\nRule #6: scissors decapitates lizard. "
      f"\nRule #7: lizard eats paper. "
      f"\nRule #8: paper disproves spock. "
      f"\nRule #9: spock vaporizes rock."
      f"\nRule #10: rock crushes scissors. "
      f"\n******************************")

import random

gamePlayed = int(input("How many games would you like to play? "))
moves = ["rock", "paper", "scissor", "lizard", "spock"]

for game in range(gamePlayed):
      computer = moves[random.randint(0, 4)]
      player = input("Enter rock, paper, scissors , lizard or spock: ").lower()
      if player == computer:
            print("Tie!")
      elif player == "rock":
            if computer == "paper":
                  print(f"CPU choose")
                  print(f"You lose! {computer} beats {player}")
            else:
                  print(f"You win! {player} beats {computer}")
      elif player == "paper":
            if computer == "scissor":
                  print(f"You lose! {computer} beats {player}")
            else:
                  print(f"You win! {player} beats {computer}")
      elif player == "scissor":
            if computer == "rock":
                  print(f"You lose! {computer} beats {player}")
            else:
                  print(f"You win! {player} beats {computer}")
      elif player == "spock":
            if computer == "lizard":
                  print(f"You lose! {computer} beats {player}")
            else:
                  print(f"You win! {player} beats {computer}")
      elif player == "rock":
            if computer == "spock":
                  print(f"You lose! {computer} beats {player}")
            else:
                  print(f"You win! {player} beats {computer}")
      elif player == "paper":
            if computer == "lizard":
                  print(f"You lose! {computer} beats {player}")
            else:
                  print(f"You win! {player} beats {computer}")
      elif player == "lizard":
            if computer == "rock":
                  print(f"You lose! {computer} beats {player}")
            else:
                  print(f"You win! {player} beats {computer}")

print("\nThank you for playing my game")
