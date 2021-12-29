import pygame
from pygame.constants import K_ESCAPE, MOUSEBUTTONDOWN
from .constants import BLACK, FONT_TITLE_BUTONS, FONT_TITLE_HEADER, GREY, SQUARE_SIZE, WHITE

class Window:
    def __init__(self, width, height, caption) -> "Window":
        pygame.init()
        self._win = pygame.display.set_mode((width, height))
        pygame.display.set_caption(f"{caption}")
        self._side = None
        self._gamemode = None
        self._action = None

    def side(self):
        return self._side

    def gamemode(self):
        return self._gamemode

    def action(self):
        return self._action

    def win(self):
        return self._win

    def check_mouse_pos(self):
        pos = pygame.mouse.get_pos()
        row, col = self.get_row_col_from_mouse(pos)
        return row, col

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y//SQUARE_SIZE
        col = x//SQUARE_SIZE
        return int(row), int(col)

    def update(self):
        pygame.display.update()

    def draw_text(self, text, font, color, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self._win.blit(textobj, textrect)

    def title_screen(self):
        run = True
        button_new_game = pygame.Rect(150, 275, 300, 100)
        button_load_game = pygame.Rect(150, 400, 300, 100)
        click = False
        while run:
            x, y = pygame.mouse.get_pos()
            self._win.fill(WHITE)
            font_title = pygame.font.SysFont(None, FONT_TITLE_HEADER)
            font_button = pygame.font.SysFont(None, FONT_TITLE_BUTONS)
            self.draw_text("CHAOS AND ORDER", font_title, BLACK, 100, 100)
            pygame.draw.rect(self._win, GREY, button_new_game)
            pygame.draw.rect(self._win, GREY, button_load_game)
            self.draw_text("New game", font_button, BLACK, 225, 310)
            self.draw_text("Load game", font_button, BLACK, 225, 435)
            if button_load_game.collidepoint((x, y)):
                if click:
                    self._action = "Load"
                    run = False
            if button_new_game.collidepoint((x, y)):
                if click:
                    self._action = "New"
                    run = False
            self.update()
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                        pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

    def side_choose_window(self):
        run = True
        button_order = pygame.Rect(150, 275, 300, 100)
        button_chaos = pygame.Rect(150, 400, 300, 100)
        click = False
        while run:
            x, y = pygame.mouse.get_pos()
            self._win.fill(WHITE)
            font_title = pygame.font.SysFont(None, FONT_TITLE_HEADER)
            font_button = pygame.font.SysFont(None, FONT_TITLE_BUTONS)
            self.draw_text("Choose side", font_title, BLACK, 160, 100)
            pygame.draw.rect(self._win, GREY, button_order)
            pygame.draw.rect(self._win, GREY, button_chaos)
            self.draw_text("Order", font_button, BLACK, 250, 310)
            self.draw_text("Chaos", font_button, BLACK, 250, 435)
            if button_chaos.collidepoint((x, y)):
                if click:
                    self._side = "Chaos"
                    run = False
            if button_order.collidepoint((x, y)):
                if click:
                    self._side = "Order"
                    run = False
            self.update()
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                        pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

    def difficulty_choose_window(self):
        run = True
        button_easy = pygame.Rect(150, 275, 300, 100)
        button_hard = pygame.Rect(150, 400, 300, 100)
        click = False
        while run:
            x, y = pygame.mouse.get_pos()
            self._win.fill(WHITE)
            font_title = pygame.font.SysFont(None, FONT_TITLE_HEADER)
            font_button = pygame.font.SysFont(None, FONT_TITLE_BUTONS)
            self.draw_text("Choose difficulty", font_title, BLACK, 125, 100)
            pygame.draw.rect(self._win, GREY, button_easy)
            pygame.draw.rect(self._win, GREY, button_hard)
            self.draw_text("Easy", font_button, BLACK, 260, 310)
            self.draw_text("Hard", font_button, BLACK, 260, 435)
            if button_hard.collidepoint((x, y)):
                if click:
                    self._gamemode = "Hard"
                    run = False
            if button_easy.collidepoint((x, y)):
                if click:
                    self._gamemode = "Easy"
                    run = False
            self.update()
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                        pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
