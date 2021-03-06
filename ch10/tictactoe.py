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
        return 'player'
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
    # Python short-ciruit evaluation. A string will never be passed into isSpaceFree.
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9): ', end='')
        move = input()
    return int(move)

# Given a list of moves, randomly pick one that is a possible move, else return None.
def getRandomeMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

# Game AI, return move number (1 - 9)
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # AI step 1. Choose the winning move, if there is one.
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # AI step 2. Block Player's winning move.
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # AI step 3. Randomly choose a free corner.
    corner = getRandomeMoveFromList(board, [1, 3, 7, 9])
    if corner:
        return corner

    # AI step 4. Choose center if it is free
    if isSpaceFree(board, 5):
        return 5

    # AI step 5. Choose a side space
    return  getRandomeMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcom to Tic-Tac-Toe')


# play again loop
while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    gameIsPlaying = True

    while gameIsPlaying:

        # player turn
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            # check if the move won the game
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('You won!')
                gameIsPlaying = False

            # is board full or computer's turn
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break

                # player done
                else:
                    turn = 'computer'

        # computer turn
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("The computer wins")
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = 'player'

    print("Do you want to play again? (Y/N): ", end='')
    if not input().upper().startswith('Y'):
        break


