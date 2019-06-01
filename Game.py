import pygame
from pygame.locals import *
from Field import *

# DIMENSIONS
BLOCK_SIZE = 100
MARGIN = 5

FPS = 60

# STATE
RUNNING = 0
GAME_OVER = 1
WIN = 2
QUIT = 3
RESTART = 4

# COLOR
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Game:

    def __init__(self, x, y, mine, cheat=False):
        self.size_x = x
        self.size_y = y
        self.nb_mine = mine
        self.cheat = cheat
        self.mine_field = None
        self.window = None

    def get_dimensions(self):
        return (BLOCK_SIZE + MARGIN) * self.size_x + MARGIN, (BLOCK_SIZE + MARGIN) * self.size_y + MARGIN

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()

        self.mine_field = Field(self.size_x, self.size_y, self.nb_mine)

        self.window = pygame.display.set_mode(self.get_dimensions())
        pygame.display.set_caption('Demineur')

        if self.cheat:
            self.print_field()

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

                    case = self.mine_field.get_case(row, column)

                    if case is not None:
                        # if left click and not flagged case
                        if click[0] == 1 and not self.mine_field.get_case(row, column).is_flag():

                            self.mine_field.open_case(row, column)

                            if case.has_mine():
                                case.explode()
                                state = GAME_OVER
                            elif self.mine_field.is_win():
                                state = WIN
                        # if right click
                        elif click[2] == 1:
                            case.toggle_flag()

            self.draw_grid()

            clock.tick(FPS)
            pygame.display.flip()

            if state == RUNNING:
                continue
            elif state == WIN:
                state = self.end(GREEN)
            elif state == GAME_OVER:
                state = self.end(RED)
            elif state == QUIT:
                pygame.time.wait(1000)
                break

        pygame.quit()

    def draw_grid(self):
        for i in range(self.size_x):
            for j in range(self.size_y):
                case = self.mine_field.get_case(i, j)
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
                                self.window.blit(img, rect)
                            else:
                                img = pygame.image.load('resource/mine.png')
                                img = pygame.transform.scale(img, (BLOCK_SIZE, BLOCK_SIZE))
                                rect = img.get_rect()
                                rect = rect.move((left, top))
                                self.window.blit(img, rect)

                        else:
                            val = case.get_value()
                            if val != '0':
                                img = pygame.image.load('resource/' + val + '.png')
                                img = pygame.transform.scale(img, (BLOCK_SIZE, BLOCK_SIZE))
                                rect = img.get_rect()
                                rect = rect.move((left, top))
                                self.window.blit(img, rect)
                            else:
                                pygame.draw.rect(self.window, GREY, rect)
                    elif case.is_flag():
                        img = pygame.image.load('resource/flag.png')
                        img = pygame.transform.scale(img, (BLOCK_SIZE, BLOCK_SIZE))
                        rect = img.get_rect()
                        rect = rect.move((left, top))
                        self.window.blit(img, rect)
                    else:
                        pygame.draw.rect(self.window, WHITE, rect)

    def end(self, back_color):
        self.mine_field.show_mines()
        self.window.fill(back_color)

        return QUIT

    def print_field(self):
        print('Mine Field')
        for x in range(self.mine_field.size_x):
            ligne = ''
            for y in range(self.mine_field.size_y):
                ligne += self.mine_field.field[x][y].value
                if y < self.mine_field.size_y - 1:
                    ligne += ' | '

            print(ligne)

