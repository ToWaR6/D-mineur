import pygame, getopt, sys
from pygame.locals import *
from Field import *
from Utils import *

pygame.init()

size_x = 3
size_y = 3
block_size = 100
margin = 5

DIMENSIONS=((block_size+margin)*size_x, (block_size+margin)*size_y)
nb_mine = 2

FPS = 30

# STATE
RUNNING = 0
GAME_OVER = 1
WIN = 2
QUIT = 3

WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


clock = pygame.time.Clock()

if nb_mine > size_x*size_y:
    print('Il y a plus de mine que de case')
    pygame.quit()


def draw_grid():
    for i in range(size_x):
        for j in range(size_y):
            case = mine_field.get_case(i, j)
            if case is not None:
                left = (block_size + margin) * j + margin
                top = (block_size + margin) * i + margin
                rect = pygame.Rect(left, top, block_size, block_size)
                if case.is_opened():
                    if case.has_mine():
                        img = pygame.image.load('resource/mine_red.png')
                        img = pygame.transform.scale(img, (block_size, block_size))
                        rect = img.get_rect()
                        rect = rect.move((left, top))
                        window.blit(img, rect)
                    else:
                        val = case.get_value()
                        if val != '0':
                            img = pygame.image.load('resource/'+val+'.png')
                            img = pygame.transform.scale(img, (block_size, block_size))
                            rect = img.get_rect()
                            rect = rect.move((left, top))
                            window.blit(img, rect)
                        else:
                            pygame.draw.rect(window, GREY, rect)
                else:
                    pygame.draw.rect(window, WHITE, rect)


def win():
    window.fill(GREEN)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('YOU WIN', True, BLACK, GREEN)
    text_rect = text.get_rect()
    text_rect.center = (DIMENSIONS[0] // 2, DIMENSIONS[1] // 2)
    window.blit(text, text_rect)


def game_over():
    window.fill(RED)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('YOU LOSE', True, BLACK, RED)
    text_rect = text.get_rect()
    text_rect.center = (DIMENSIONS[0] // 2, DIMENSIONS[1] // 2)
    window.blit(text, text_rect)


window = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_caption('Demineur')

mine_field = Field(size_x, size_y, nb_mine)

print_field(mine_field)

state = RUNNING
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = QUIT
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (block_size + margin)
            row = pos[1] // (block_size + margin)
            # Set that location to one

            mine_field.open_case(row, column)

            case = mine_field.field[row][column]
            if case.has_mine():
                state = GAME_OVER
            elif mine_field.is_win():
                state = WIN

    if state == RUNNING:
        draw_grid()
    elif state == WIN:
        win()
    elif state == GAME_OVER:
        game_over()
    elif state == QUIT:
        break

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()