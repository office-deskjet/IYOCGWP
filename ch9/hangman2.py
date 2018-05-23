import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''','''
  +---+
  O   |
      |
      |
     ===''','''
  +---+
  O   |
  |   |
      |
     ===''','''
  +---+
  O   |
 /|   |
      |
     ===''','''
  +---+
  O   |
 /|\  |
      |
     ===''','''
  +---+
  O   |
 /|\  |
 /    |
     ===''','''
  +---+
  O   |
 /|\  |
 / \  |
      |
     ===''','''
  +---+
 [O   |
 /|\  |
 / \  |
      |
     ===''','''
  +---+
 [O]  |
 /|\  |
 / \  |
      |
     ===''']


# {string:List of Strings}
words = {
'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':('square triangle rectangle circle ellipse rhombus trapazoid chevron ' 
            'pentagon hexagon septagon octogon').split(),
'Fruits':('apple orange lemon lime pear watermelon grape grapefruit cherry banana ' 
            'cantalope mango strawberry tomato').split(),
'Animals':('bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog '
            'goat leech lion lizard monkey moose mouse otter owl panda python rabbit '
            'rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra').split()
}

# Retrun a list of a random word from passed in word dictionary and its key.
def getRandomWord(wordDict):
    key = random.choice(list(wordDict.keys()))
    word = random.choice(wordDict[key])

    return [word, key]


# draw the hangman, missed letters, correct letters, and blanks in the word.
def displayBoard(missedLetters, correctLetters, secretWord):
    # will go out of bounds
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Missed letters:", end=" ")
    for letter in missedLetters:
        print(letter, end=" ")
    print()

    #build hint
    blanks = "_" * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            # string builder: take everything before i, insert sercret letter + take everything after i
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    print("Secret word:", end=" ")
    for letter in blanks:
        print(letter, end=" ")
    print()

# Retrun letter the palyer guessed. Validates to a single letter.
def getGuess(alreadyGuessed):
    while True:
        print("Guess a letter: ", end ="")
        guess = input()
        guess = guess.lower()

        if len(guess) != 1:
            print("Please enter a singple letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a letter.")
        else:
            return guess


# run the game again if Y
def playAgain():
    print("Do you want to play again (Y/N)? ", end ="")
    return input().lower().startswith("y")

def setDifficulty():
    difficulty = " "
    while difficulty not in "EMH":
        print("Enter difficulty: (E)asy, (M)edium, (H)ard: ", end="")
        difficulty = input().upper()

    if difficulty == 'M':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]

    elif difficulty == 'H':
        for i in range(4):
            del HANGMAN_PICS[3]

# start of program
print("H A N G M A N")
missedLetters = ""
correctLetters = ""
secretWord, wordCatagory = getRandomWord(words)
gameIsDone = False
setDifficulty()

# main game loop
while True:
    print('The secret word is in the catagory: ' + wordCatagory)
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Did player win?
        foundAllletters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllletters = False

        if foundAllletters:
            print("You guess correct!. The secret word is " + secretWord + "! You win!")
            gameIsDone = True


    else:
        missedLetters = missedLetters + guess
        
        # Did player lose?
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print("You ran out of guesses!")
            print("After " + str(len(missedLetters)) + "missed guess and " + 
                str(len(correctLetters)) + " correct guess, the secret word was '" + secretWord + "'")
            gameIsDone = True

    # play again?
    if gameIsDone:
        if playAgain():
            missedLetters = ""
            correctLetters = ""
            secretWord, wordCatagory = getRandomWord(words)
            gameIsDone = False
        else:
            break


