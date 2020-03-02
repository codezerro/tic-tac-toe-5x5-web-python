from enum import Enum
import datetime
import random
import pygame

pygame.init()
"""
draw board
"""

win = pygame.display.set_mode((900, 900))

pygame.display.set_caption('tic ')

first = pygame.draw.rect(win, (255, 255, 255), (25, 25, 150, 150))
second = pygame.draw.rect(win, (255, 255, 255), (200, 25, 150, 150))
third = pygame.draw.rect(win, (255, 255, 255), (375, 25, 150, 150))
four = pygame.draw.rect(win, (255, 255, 255), (550, 25, 150, 150))
five = pygame.draw.rect(win, (255, 255, 255), (725, 25, 150, 150))

six = pygame.draw.rect(win, (255, 255, 255), (25, 200, 150, 150))
seven = pygame.draw.rect(win, (255, 255, 255), (200, 200, 150, 150))
eight = pygame.draw.rect(win, (255, 255, 255), (375, 200, 150, 150))
nine = pygame.draw.rect(win, (255, 255, 255), (550, 200, 150, 150))
ten = pygame.draw.rect(win, (255, 255, 255), (725, 200, 150, 150))

eleven = pygame.draw.rect(win, (255, 255, 255), (25, 375, 150, 150))
tweleve = pygame.draw.rect(win, (255, 255, 255), (200, 375, 150, 150))
thriten = pygame.draw.rect(win, (255, 255, 255), (375, 375, 150, 150))
fourthen = pygame.draw.rect(win, (255, 255, 255), (550, 375, 150, 150))
fithen = pygame.draw.rect(win, (255, 255, 255), (725, 375, 150, 150))

sixthen = pygame.draw.rect(win, (255, 255, 255), (25, 550, 150, 150))
seventen = pygame.draw.rect(win, (255, 255, 255), (200, 550, 150, 150))
eighten = pygame.draw.rect(win, (255, 255, 255), (375, 550, 150, 150))
nineten = pygame.draw.rect(win, (255, 255, 255), (550, 550, 150, 150))
twenty = pygame.draw.rect(win, (255, 255, 255), (725, 550, 150, 150))

twentyOne = pygame.draw.rect(win, (255, 255, 255), (25, 550, 150, 150))
twentyTwo = pygame.draw.rect(win, (255, 255, 255), (200, 550, 150, 150))
twentyThree = pygame.draw.rect(win, (255, 255, 255), (375, 550, 150, 150))
twentyFour = pygame.draw.rect(win, (255, 255, 255), (550, 550, 150, 150))
twentyfive = pygame.draw.rect(win, (255, 255, 255), (725, 550, 150, 150))

# win = pygame.display.set_mode((900, 900))

# pygame.display.set_caption('tic ')

"""Constants"""
PLAYER = 'X'
COMPUTER = 'O'
EMPTY = '_'
BOARD_SIZE = 5
NUMBER_OF_PLAYERS = 1
SEARCH_TIME = 5
VALUE_HERE = 1

"""exception class, in case the user entered a none empty position"""


class NoneEmptyPosition(Exception):
    pass


"""exception class, in case the user entered number higher the board positions"""


class OutOfRange(Exception):
    pass

# Game State


class GameState(Enum):
    tie = 'Tie'
    notEnd = 'notEnd'
    o = 'O'  # computer won
    x = 'X'  # player won


class Board:

    """
        the constructor gets 1 argumnet size - the size of the board
        it initialized the game board to be empty board (size x size)
        and store the last move which been made in order to decide who won
        """

    def __init__(self, size):
        self.mSize = size
        self.mBoard = [
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            [' ', ' ', ' ', ' ', ' ']
        ]  # [[EMPTY for x in range(size)] for y in range(size)]
        self.lastMove = None

    """this function prints the game board"""

    # def print(self):
    #     for i in range(self.mSize):
    #         for j in range(self.mSize):
    #             if j < self.mSize-1:
    #                 print(self.mBoard[i][j], end='|')
    #             else:
    #                 print(self.mBoard[i][j], end='')
    #         print()
    # def draw_board(self):
    #     for i in range(5):
    #         for j in range(5):
    #             if self.mBoard[i][j] == 'X':
    #                 print('hello')
    #                 pygame.draw.rect(win, (255, 0, 0), (50, 50, 100, 100))

    """this function gets position 0 - size x size
            and convert it to a board position
            and return the match row and column"""

    def getBoardPosition(self, position):

        column = position % self.mSize
        row = position//self.mSize
        return row, column

    """this function return the last move on the board"""

    def getLastMove(self):
        return self.lastMove

    """this function gets number of row in the board and return the match row"""

    # todo crop

    """this function gets position and draw 'X' on the match place on the board"""

    def drawX(self, position):
        self.lastMove = position
        (row, column) = self.getBoardPosition(position)
        self.mBoard[row][column] = PLAYER
        print(row)
        # self.draw_board()

    """this function gets position and draw '_' on the match place on the board"""

    def drawEmpty(self, position):
        (row, column) = self.getBoardPosition(position)
        self.mBoard[row][column] = EMPTY

    """this function gets position and draw 'O' on the match place on the board"""

    def drawO(self, position):
        self.lastMove = position
        (row, column) = self.getBoardPosition(position)
        self.mBoard[row][column] = COMPUTER
        # self.draw_board()

    """this function gets position and checking if it empty"""

    def checkIfRubricEmpty(self, position):
        (row, column) = self.getBoardPosition(position)
        return self.mBoard[row][column] == EMPTY

    """this function gets 2 arguments:  listToBeChecked - line in the board
            char - 'X' or 'Y' and checking if all the line filled with it"""

    def all_same(self, listToBeChecked, char):
        return all(x == char for x in listToBeChecked)

    """this define wins state """

    def wins(self, mBoard, player):
        winList = [
            [self.mBoard[0][0], self.mBoard[1][1], self.mBoard[2]
                [2], self.mBoard[3][3], self.mBoard[4][4]],
            [self.mBoard[0][0], self.mBoard[0][1], self.mBoard[0]
                [2], self.mBoard[0][3], self.mBoard[0][4]],
            [self.mBoard[0][0], self.mBoard[1][0], self.mBoard[2]
                [0], self.mBoard[3][0], self.mBoard[4][0]],
            [self.mBoard[0][1], self.mBoard[1][1], self.mBoard[2]
                [1], self.mBoard[3][1], self.mBoard[4][1]],
            [self.mBoard[0][2], self.mBoard[1][2], self.mBoard[2]
                [2], self.mBoard[3][2], self.mBoard[4][2]],
            [self.mBoard[0][3], self.mBoard[1][3], self.mBoard[2]
                [3], self.mBoard[3][3], self.mBoard[4][3]],
            [self.mBoard[0][4], self.mBoard[1][4], self.mBoard[2]
                [4], self.mBoard[3][4], self.mBoard[4][4]],
            [self.mBoard[1][0], self.mBoard[1][1], self.mBoard[1]
                [2], self.mBoard[1][3], self.mBoard[1][4]],
            [self.mBoard[2][0], self.mBoard[2][1], self.mBoard[2]
                [2], self.mBoard[2][3], self.mBoard[2][4]],
            [self.mBoard[3][0], self.mBoard[3][1], self.mBoard[3]
                [2], self.mBoard[3][3], self.mBoard[3][4]],
            [self.mBoard[4][0], self.mBoard[4][1], self.mBoard[4]
                [2], self.mBoard[4][3], self.mBoard[4][4]],
            [self.mBoard[0][4], self.mBoard[1][3], self.mBoard[2]
                [2], self.mBoard[3][1], self.mBoard[4][0]]
        ]

        if [player, player, player, player, player] in winList:
            return True
        else:
            return False


"""this class handling all the game Activities"""


class Game:
    """the constructor gets 2 arguments: numberOfPlayers, board size
        also, mNamesList - store the names of the players
        mTurn - says who have the turn to play, even -player1, odd - player2
        mComputerFirstPosition - store the random position of the computer"""

    def __init__(self, numberOfPlayers, boardSize):
        self.mBoard = Board(boardSize)
        self.mBoardSize = boardSize
        self.mNumberOfPlayers = numberOfPlayers
        self.mNamesList = 'None'  # [' ']*numberOfPlayers
        self.mTurn = None
        self.mComputerFirstPosition = None
        self.coinFlip()
        self.mBestMove = 0

    """this function decide who is starting the game by coin flip,
            if the computer won it choose random Move for the first move"""

    def coinFlip(self):
        # turn = random.choice(['computer', 'player'])
        turn = 'player'
        if turn == 'computer':
            self.mComputerFirstPosition = random.randrange(
                self.mBoard.mSize ** 2)
            self.mTurn = 1
        else:
            self.mTurn = 0

    """this function gets the player move from the user"""

    def getPlayerMove(self):
        while True:
            try:
                playerMove = int(
                    input(self.mNamesList[self.mTurn] + ' please select rubric'))
                if not (0 <= playerMove <= (self.mBoardSize ** 2 - 1)):
                    raise OutOfRange(
                        "Wrong position, please choose position 0 - " + str(self.mBoardSize ** 2 - 1))

                if not self.mBoard.checkIfRubricEmpty(playerMove):
                    raise NoneEmptyPosition(
                        "this rubric taken please choose other rubric")

                return playerMove

            except (OutOfRange, NoneEmptyPosition) as e:
                print(e)
            except ValueError as e:
                print("only numbers are allowed")
            except Exception:
                print("unknown error")

    """ this function gets a player turn and check if the player won
        based on his last move, it checking every line which including the last move"""

    def checkForWin(self, turn):
        char = ''
        if turn % 2 == 0:
            char = 'X'
        else:
            char = 'O'
        return self.mBoard.wins(self.mBoard.mBoard, char)

    """this function check if the game is tie, which means the board is filled and there is no winner"""

    def checkForTie(self):
        for i in range(self.mBoard.mSize ** 2):
            if self.mBoard.checkIfRubricEmpty(i):
                return False
        return True

    """this function compute all the valid moves on the game board and return them"""

    def genrate(self):
        possibleMoves = []
        for i in range(self.mBoard.mSize ** 2):
            if self.mBoard.checkIfRubricEmpty(i):
                possibleMoves.append(i)
        return possibleMoves

    """this function check the game state and return it"""

    def checkGameState(self):
        if self.checkForWin(0):
            return GameState.x

        if self.checkForWin(1):
            return GameState.o

        if self.checkForTie():
            return GameState.tie

        return GameState.notEnd

    """ this function is starting the game and managing it until it over"""

    def start(self):
        # self.getPlayersNames()
        human = True
        run = True
        while run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        canPlay = True
                if human:
                    human = False
                    print('human')
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if first.collidepoint(pos):
                            playerMove = 0
                            human = False
                            self.mBoard.drawX(playerMove)

                elif not human:
                    print('computer please select rubric')
                    if self.mComputerFirstPosition is not None:
                        computerMove = self.mComputerFirstPosition
                        self.mComputerFirstPosition = None
                    else:
                        computerMove = self.iterativeDeepSearch()
                    human = True
                    self.mBoard.drawO(computerMove)

            pygame.display.update()
        pygame.quit()

    """ this function gets 6 arguments: depth - the depth of the game tree
        isMax - tell which side are we, the maximizer or the minimizer
        alpha - store the best value for the maximizer
        beta - store the best value for the minimizer
        startTime - the time we started the search
        timeLimit - the time we will search for the best move
        the function tells if the moves I take is better or worse by compute the best score
        and position in the given depth, than it return them
        I used minmax algorithm with alpha beta pruning"""

    def minmax2(self, depth, isMax, alpha, beta, startTime, timeLimit):
        # print(timeLimit)
        moves = self.genrate()
        # print(moves)
        score = self.evaluate()
        position = None

        if datetime.datetime.now() - startTime >= timeLimit:
            self.mTimePassed = True

        if not moves or depth == 0 or self.mTimePassed:
            gameResult = self.checkGameState()
            if gameResult.value == 'X':
                return -10**(self.mBoard.mSize+1), position
            elif gameResult.value == 'O':
                return 10**(self.mBoard.mSize+1), position
            elif gameResult.value == 'Tie':
                return 0, position
            return score, position

        if isMax:
            for i in moves:
                self.mBoard.drawO(i)
                score, dummy = self.minmax2(
                    depth-1, not isMax, alpha, beta, startTime, timeLimit)
                if score > alpha:
                    alpha = score
                    position = i
                    self.mBestMove = i

                self.mBoard.drawEmpty(i)
                if beta <= alpha:
                    break

            return alpha, position
        else:
            for i in moves:
                self.mBoard.drawX(i)
                score, dummy = self.minmax2(
                    depth-1, not isMax, alpha, beta, startTime, timeLimit)
                if score < beta:
                    beta = score
                    position = i
                    self.mBestMove = i
                self.mBoard.drawEmpty(i)
                if alpha >= beta:
                    break

            return beta, position

    # """this function search the best move it find in 5 seconds.
    #    The function goes as deep as possible in 5 second in the game tree
    #    and return the best move"""

    def iterativeDeepSearch(self):
        startTime = datetime.datetime.now()
        # print(startTime)
        endTime = startTime + datetime.timedelta(0, SEARCH_TIME)
        # print(endTime)
        depth = 1
        position = None
        self.mTimePassed = False
        while True:
            currentTime = datetime.datetime.now()
            if currentTime >= endTime:
                break
            best, position = self.minmax2(
                depth, True, -10000000, 10000000, currentTime, endTime-currentTime)
            depth += 1

        if position is None:
            position = self.mBestMove

        return position

    # """this function gets a board line and calculate how many
    #     'X', 'O' and empty rubrics"""

    # def calculateLine(self, line):
    #     oSum = line.count(COMPUTER)
    #     xSum = line.count(PLAYER)
    #     EmptySum = line.count(EMPTY)
    #     return oSum, xSum, EmptySum

    """this function gets a board line and calculate it score"""

    def getScoreLine(self, mBoard):
        score = 0
        xSum = 0
        oSum = 0
        EmptySum = 0
        for i in range(5):
            for j in range(5):
                if mBoard[i][j] == 'x':
                    xSum += 1
                elif mBoard[i][j] == 'o':
                    oSum += 1
                else:
                    EmptySum += 1
        # oSum, xSum, EmptySum = self.calculateLine(line)
        if xSum == 0 and oSum != 0:
            if oSum == self.mBoard.mSize:
                score += 11 ** (oSum - 1)
            score += 10 ** (oSum - 1)
        if oSum == 0 and xSum != 0:
            score += -(10 ** (xSum - 1))
        return score

    """this function evaluate the game board and return the score"""

    def evaluate(self):
        score = 0
        # for i in range(self.mBoard.mSize):
        score += self.getScoreLine(self.mBoard.mBoard)
        # score += self.getScoreLine(self.mBoard.mBoard)

        # diagonals = self.mBoard.getDiagonal()
        # for i in range(2):
        #     score += self.getScoreLine(diagonals[i])

        return score


game = Game(NUMBER_OF_PLAYERS, BOARD_SIZE)
game.start()

pygame.quit()
