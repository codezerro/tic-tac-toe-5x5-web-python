import pygame
pygame.init()


# define board
board = [[None, None, None], [None, None, None], [None, None, None]]

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


# def draw_board():
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == 'X':
#                 print('hello')
#                 pygame.draw.rect(win, (255, 0, 0), (50, 50, 100, 100))


# print(start_game())

run = True
# while run:
  pygame.time.delay(100)
#    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if first.collidepoint(pos):
                board[0][0] = 'X'
                draw_board()

            if second.collidepoint(pos):
                board[0][1] = 'X'
                draw_board()
            if third.collidepoint(pos):
                board[0][2] = 'X'
                draw_board()

            if four.collidepoint(pos):
                board[1][0] = 'X'
                draw_board()

            if five.collidepoint(pos):
                board[1][1] = 'X'
                draw_board()
            if six.collidepoint(pos):
                board[1][2] = 'X'
                draw_board()

            if seven.collidepoint(pos):
                board[2][0] = 'X'
                draw_board()

            if eight.collidepoint(pos):
                board[2][1] = 'X'
                draw_board()
            if nine.collidepoint(pos):
                board[2][2] = 'X'
                draw_board()

    pygame.display.update()
# end loop


pygame.quit()
