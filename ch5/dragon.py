# choose between two caves of dragons, death or treasure!
import random
import time

def displayIntro():
    # ''' means muliline string
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon 
is greedy and hungry, and will eat you on sight.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print("Which cave do you enter? (1 or 2): ", end="")
        cave = input()

chosenCave = chooseCave()
displayIntro()