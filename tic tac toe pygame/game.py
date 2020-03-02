import pygame
import sys
# © 2019 TheFlyingKeyboard and released under MIT License
# theflyingkeyboard.net


def map_mouse_to_board(x, y):
    if x < gameSize / 3:
        column = 0
    elif gameSize / 3 <= x < (gameSize / 3) * 2:
        column = 1
    else:
        column = 2
    if y < gameSize / 3:
        row = 0
    elif gameSize / 3 <= y < (gameSize / 3) * 2:
        row = 1
    else:
        row = 2
    return column, row


def draw_board(board):
    myFont = pygame.font.SysFont('Tahoma', gameSize // 3)
    for y in range(3):
        for x in range(3):
            if board[y][x] == xMark:
                color = xColor
            else:
                color = oColor
            text_surface = myFont.render(board[y][x], False, color)
            screen.blit(text_surface, (y * (gameSize // 3) + margin +
                                       (gameSize // 18), x * (gameSize // 3) + margin))


def is_full(board):
    return not any(None in sublist for sublist in board)


def get_winner(board):
    # Diagonals
    if ((board[0][0] == board[1][1] and board[1][1] == board[2][2])
            or (board[0][2] == board[1][1] and board[1][1] == board[2][0])) and board[1][1] is not None:
        return board[1][1]
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] is not None:  # Rows
            return board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] is not None:  # Columns
            return board[0][i]
    return None


def draw_lines():
    # Vertical lines
    pygame.draw.line(screen, lineColor, (margin + gameSize // 3, margin),
                     (margin + gameSize // 3, screenSize - margin), lineSize)
    pygame.draw.line(screen, lineColor, (margin + (gameSize // 3) * 2, margin),
                     (margin + (gameSize // 3) * 2, screenSize - margin), lineSize)
    # Horizontal lines
    pygame.draw.line(screen, lineColor, (margin, margin + gameSize // 3), (screenSize - margin, margin + gameSize // 3),
                     lineSize)
    pygame.draw.line(screen, lineColor, (margin, margin + (gameSize // 3) * 2),
                     (screenSize - margin, margin + (gameSize // 3) * 2), lineSize)


screenSize = 700
margin = 10
gameSize = 700 - (2 * margin)
lineSize = 10
backgroundColor = (0, 0, 0)
lineColor = (255, 255, 255)
xColor = (200, 0, 0)
oColor = (0, 0, 200)
xMark = 'X'
oMark = 'o'
board = [[None, None, None], [None, None, None], [None, None, None]]
currentMove = 'X'
pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize))
pygame.display.set_caption("Tic Tac Toe")
pygame.font.init()
myFont = pygame.font.SysFont('Tahoma', gameSize // 3)
screen.fill(backgroundColor)
canPlay = True
draw_lines()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                board = [[None, None, None], [
                    None, None, None], [None, None, None]]
                screen.fill(backgroundColor)
                draw_lines()
                canPlay = True
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type is pygame.MOUSEBUTTONDOWN and canPlay:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            (column, row) = map_mouse_to_board(mouseX, mouseY)
            if board[column][row] is None:
                board[column][row] = currentMove
                if currentMove == xMark:
                    currentMove = oMark
                else:
                    currentMove = xMark
                draw_board(board)
                winner = get_winner(board)
                if winner is not None:
                    myFont = pygame.font.SysFont('Tahoma', screenSize // 5)
                    text_surface = myFont.render(
                        str(winner) + " has won!", False, lineColor)
                    screen.blit(
                        text_surface, (margin, screenSize // 2 - screenSize // 10))
                    canPlay = False
                else:
                    if is_full(board):
                        myFont = pygame.font.SysFont('Tahoma', screenSize // 5)
                        text_surface = myFont.render("Draw!", False, lineColor)
                        screen.blit(text_surface, (screenSize // 10,
                                                   screenSize // 2 - screenSize // 10))
    pygame.display.update()
