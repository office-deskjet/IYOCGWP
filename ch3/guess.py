# this is a number guessing game
import random

guessesTaken = 0
START = 1
STOP = 20
MAX_GUESSES = 6
number = random.randint(1, 20)

print("Hello, what is your name?")
playerName = input()
print(playerName + ", I am thinking of a number between " + str(START) + " and " + str(STOP))

for i in range(MAX_GUESSES):
    print("guess")
pass

