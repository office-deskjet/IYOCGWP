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
    return cave

def checkCave(chosenCave):
    print("You approach the cave...")
    time.sleep(1)

    print("It is dark and spooky...")
    time.sleep(1)

    print("A large dragon jumps out in front of you! He opens his jaws and..")
    print()
    time.sleep(2)

    # returns an int
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print("Gives you his treasure!")
    else:
        print("Gobels you up in one bite!")

    
displayIntro()
chosenCave = chooseCave()
checkCave(chosenCave)
