from ast import Or
from http.client import CONTINUE
from operator import truediv
from optparse import Option
from pickle import TRUE
from pickletools import optimize
import random
from ssl import Options

user_wins = 0
computer_wins = 0

Options = ["rock","paper","scissors"]

while TRUE:
    user_input = input("type rock/paper/scissors pr q to quit").lower()
    if user_input == 'Q':
        break

    if user_input not in Options:
        continue

    random_numbers = random.randint(0,2)
    #rock: 0, paper: 1, scissors: 2
    computer_pick = Options[random_numbers]
    print("computer picked", computer_pick + ".")

    if user_input == 'rock' and computer_pick == 'scissors':
        print("YOU WON!!!")
        user_wins += 1
        

    elif user_input == 'paper' and computer_pick == 'rock':
        print("YOU WON!!!")
        user_wins += 1

    elif user_input == 'scissors' and computer_pick == 'paper':
        print("YOU WON!!!")
        user_wins += 1

    else: 
        print("YOU LOST!!!")
        computer_wins += 1

print("YOU WON!!!", user_wins, "times")
print("COMPUTER WINS!!!", computer_wins, "times")
print("GOODBYE!!!!!!")
