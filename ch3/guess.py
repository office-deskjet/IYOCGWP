# this is a number guessing game
import random

START = 1
STOP = 20
MAX_GUESSES = 6
number = random.randint(1, 20)

print("Hello, what is your name?")
playerName = input()
print(playerName + ", I am thinking of a number between " + str(START) + " and " + str(STOP))

for i in range(MAX_GUESSES):
    print("Guess the number: ")
    guess = input()
    guess = int(guess)
    
    if guess < number:
        print("Your guess is too low.")

    if guess > number:
        print("Your guess is too high.")

    if guess == number:
        break

if guess == number:
    guessTaken = i + 1
    guessTaken = str(guessTaken)
    print("Good job " + playerName + "! you guess the number in " + guessTaken + " guesses.")
else:
    number = str(number)
    print("Sorry, the correct number was " + number + ".")

