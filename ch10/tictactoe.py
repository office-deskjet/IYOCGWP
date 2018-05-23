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

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'palyer'
    else:
        return 'computer'

# place a letter at the lovcation move (1 - 9)
def makeMove(board, letter, move):
    board[move] = letter


# deterim who one, brd = game board, ltr = letter (player or computer)
def isWinner(brd,ltr):
    return ((brd[7] == ltr and brd[8] == ltr and brd[9] == ltr) or  # top row
    (brd[4] == ltr and brd[5] == ltr and brd[6] == ltr) or          # middle row
    (brd[1] == ltr and brd[2] == ltr and brd[3] == ltr) or          # bottom row
    (brd[7] == ltr and brd[4] == ltr and brd[1] == ltr) or          # left column
    (brd[8] == ltr and brd[5] == ltr and brd[2] == ltr) or          # center column
    (brd[9] == ltr and brd[6] == ltr and brd[3] == ltr) or          # right column
    (brd[7] == ltr and brd[5] == ltr and brd[3] == ltr) or          # Left right diagonal
    (brd[9] == ltr and brd[5] == ltr and brd[1] == ltr))            # right left diagonal

# return a list reference to a copy of the board game's current state
def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

# Return true if the given move is free on the board
def isSpaceFree(board, move):
    return board[move] == ' '

# limit input to 1 thru 9, and check if space free
def getPlayerMove(board):
    move = ' '
    # Python short-ciruit evaluation. A string will never be passed into isSPaceFree.
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9): ', end='')
        move = input()
    return int(move)

# Given a list of moves, randomly pick one that is a possible move, else return None.
def get RandomeMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSPaceFree(board, i):
            possibleMoves.append(i)

    if lent(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

# Game AI, return move number (1 - 9)
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

   for i in range(1,10):
       boardCopy = getBoardCopy(board)
       if isSPaceFree(boardCopy, i):
           makeMove(boardCopy, i)
           if isWinner(boardCopy, computerLetter):
               return i

