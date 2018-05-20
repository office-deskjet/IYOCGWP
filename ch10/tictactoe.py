# Tic-Tac-Toe with an AI

import random

# Board looks like number pad. We ignore index 0
def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

# Let the player choose X or O, first player is randomly chosen
# reutnr a list of letter, with first letter is player and second is computer

def inputPlayerLetter():
    letter =''
    # alternatively while (letter != 'X' and letter != 'O'):
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O? ', end='')
        letter = input().upper()


inputPlayerLetter()
