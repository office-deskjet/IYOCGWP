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
     ===''']


words = ("ant baboon badger bat bear beaver camel cat clam cobra cougar coyote "
        "crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion "
        "lizard llama mole monkey moose mouse mule newt otter owl panda parrot "
        "pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk "
        "sloth snake spider stork swan tiger toad trout turkey turtle weasel "
        "whale wolf wombat zebra").split()

# Retrun random word from passed in wordList.
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

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


# start of program
print("H A N G M A N")
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(words)
gameIsDone = False

# main game loop
while True:
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
            secretWord = getRandomWord(words)
            gameIsDone = False
        else:
            break


