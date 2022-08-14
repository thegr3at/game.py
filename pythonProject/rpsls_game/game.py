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
winStates = {"scissor": ["paper", "lizard"],
              "paper": ["rock", "spock"],
              "rock": ["lizard", "scissor"],
              "lizard": ["spock", "paper"],
              "spock": ["scissor", "rock"]}

for game in range(gamePlayed):
      computer = moves[random.randint(0, 4)]
      player = input("Enter rock, paper, scissors , lizard or spock: ").lower()
      while player not in moves:
            print("Please enter a valid input.")
            player = input("Enter rock, paper, scissors , lizard or spock: ").lower()
      if player == computer:
            print("Tie!")
      elif computer in winStates[player]:
            print(f"You win! {player} beats {computer}")
      else:
            print(f"You lose! {computer} beats {player}")

print("\nThank you for playing my game")
