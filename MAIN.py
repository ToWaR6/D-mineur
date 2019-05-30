import pygame
from pygame.locals import *
from Field import *
from Utils import *

# TODO define var from parameters
size_x = 10
size_y = 10
nb_mine = 10

# DIMENSIONS
BLOCK_SIZE = 100
MARGIN = 5
WINDOW_DIMENSIONS = ((BLOCK_SIZE + MARGIN) * size_x + MARGIN, (BLOCK_SIZE + MARGIN) * size_y + MARGIN)

FPS = 60

# STATE
RUNNING = 0
GAME_OVER = 1
WIN = 2
QUIT = 3

# COLOR
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# FUNCTIONS
def run():
    pygame.init()
    clock = pygame.time.Clock()

    if nb_mine > size_x * size_y:
        print('Il y a plus de mine que de case')
        pygame.quit()

    # if you wanna cheat:
    # print_field(mine_field)

    state = RUNNING
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            elif state == RUNNING and event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                column = pos[0] // (BLOCK_SIZE + MARGIN)
                row = pos[1] // (BLOCK_SIZE + MARGIN)

                case = mine_field.field[row][column]

                # if left click and not flagged case
                if click[0] == 1 and not mine_field.get_case(row, column).is_flag():

                    mine_field.open_case(row, column)

                    if case.has_mine():
                        case.explode()
                        state = GAME_OVER
                    elif mine_field.is_win():
                        state = WIN
                # if right click
                elif click[2] == 1:
                    case.toggle_flag()

        draw_grid()

        clock.tick(FPS)
        pygame.display.flip()

        if state == RUNNING:
            continue
        elif state == WIN:
            win()
        elif state == GAME_OVER:
            game_over()
        elif state == QUIT:
            break

    pygame.quit()


def draw_grid():
    for i in range(size_x):
        for j in range(size_y):
            case = mine_field.get_case(i, j)
            if case is not None:
                left = (BLOCK_SIZE + MARGIN) * j + MARGIN
                top = (BLOCK_SIZE + MARGIN) * i + MARGIN
                rect = pygame.Rect(left, top, BLOCK_SIZE, BLOCK_SIZE)
                if case.is_opened():
                    if case.has_mine():
                        if case.has_explode():
                            img = pygame.image.load('resource/mine_red.png')
                            img = pygame.transform.scale(img, (BLOCK_SIZE, BLOCK_SIZE))
                            rect = img.get_rect()
                            rect = rect.move((left, top))
                            window.blit(img, rect)
                        else:
                            img = pygame.image.load('resource/mine.png')
                            img = pygame.transform.scale(img, (BLOCK_SIZE, BLOCK_SIZE))
                            rect = img.get_rect()
                            rect = rect.move((left, top))
                            window.blit(img, rect)

                    else:
                        val = case.get_value()
                        if val != '0':
                            img = pygame.image.load('resource/'+val+'.png')
                            img = pygame.transform.scale(img, (BLOCK_SIZE, BLOCK_SIZE))
                            rect = img.get_rect()
                            rect = rect.move((left, top))
                            window.blit(img, rect)
                        else:
                            pygame.draw.rect(window, GREY, rect)
                elif case.is_flag():
                    img = pygame.image.load('resource/flag.png')
                    img = pygame.transform.scale(img, (BLOCK_SIZE, BLOCK_SIZE))
                    rect = img.get_rect()
                    rect = rect.move((left, top))
                    window.blit(img, rect)
                else:
                    pygame.draw.rect(window, WHITE, rect)


def win():
    # TODO dialog win w/ bouton restart/quit
    mine_field.show_mines()
    window.fill(GREEN)
    # font = pygame.font.Font('freesansbold.ttf', 32)
    # text = font.render('YOU WIN', True, BLACK, GREEN)
    # text_rect = text.get_rect()
    # text_rect.center = (WINDOW_DIMENSIONS[0] // 2, WINDOW_DIMENSIONS[1] // 2)
    # window.blit(text, text_rect)


def game_over():
    # TODO dialog game over w/ bouton restart/quit
    mine_field.show_mines()
    window.fill(RED)
    # font = pygame.font.Font('freesansbold.ttf', 32)
    # text = font.render('YOU LOSE', True, BLACK, RED)
    # text_rect = text.get_rect()
    # text_rect.center = (WINDOW_DIMENSIONS[0] // 2, WINDOW_DIMENSIONS[1] // 2)
    # window.blit(text, text_rect)


# START APP
window = pygame.display.set_mode(WINDOW_DIMENSIONS)
pygame.display.set_caption('Demineur')

mine_field = Field(size_x, size_y, nb_mine)

run()