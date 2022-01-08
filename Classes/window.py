import pygame
from pygame.constants import K_ESCAPE, MOUSEBUTTONDOWN
from os.path import exists
from .constants import BLACK, BUTTON_1_CORDS, BUTTON_2_CORDS, BUTTON_HEIGHT, BUTTON_WIDTH, FONT_TITLE_BUTONS, FONT_TITLE_HEADER, GREEN, GREY, PATH, SQUARE_SIZE, WHITE


class Window:
    def __init__(self, width, height, caption) -> "Window":
        pygame.init()
        self._win = pygame.display.set_mode((width, height))
        pygame.display.set_caption(f"{caption}")
        self._side = None
        self._gamemode = None
        self._action = None
        self._end_action = None
        self._is_save = None
        self.check_save()

    def end_action(self):
        return self._end_action

    def side(self):
        return self._side

    def gamemode(self):
        return self._gamemode

    def action(self):
        return self._action

    def win(self):
        return self._win

    def check_save(self):
        if exists(f"{PATH}"):
            self._is_save = True
        else:
            self._is_save = False

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

    def draw_text_v2(self, text, font, color, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect(center=(BUTTON_WIDTH//2, y + BUTTON_HEIGHT//2))
        #textrect.center = (x + BUTTON_WIDTH/2, y + BUTTON_HEIGHT/2)
        self._win.blit(textobj, textrect)

    def generate_basic_window(self, text_title, text_button_1, text_button_2):
        run = True
        button_new_game = pygame.Rect(BUTTON_1_CORDS[0], BUTTON_1_CORDS[1], BUTTON_WIDTH, BUTTON_HEIGHT)
        button_load_game = pygame.Rect(BUTTON_2_CORDS[0], BUTTON_2_CORDS[1], BUTTON_WIDTH, BUTTON_HEIGHT)
        click = False
        while run:
            x, y = pygame.mouse.get_pos()
            self._win.fill(WHITE)
            font_title = pygame.font.SysFont(None, FONT_TITLE_HEADER)
            font_button = pygame.font.SysFont(None, FONT_TITLE_BUTONS)
            self.draw_text_v2(f"{text_title}", font_title, BLACK, 100, 100)
            pygame.draw.rect(self._win, GREY, button_new_game)
            pygame.draw.rect(self._win, GREY, button_load_game)
            self.draw_text(f"{text_button_1}", font_button, BLACK, 225, 310)
            self.draw_text(f"{text_button_2}", font_button, BLACK, 225, 435)
            if button_load_game.collidepoint((x, y)):
                if self._is_save:
                    pygame.draw.rect(self._win, GREEN, button_load_game)
                    self.draw_text("Load game", font_button, BLACK, 225, 435)
                    if click:
                        self._action = "Load"
                        run = False
            if button_new_game.collidepoint((x, y)):
                pygame.draw.rect(self._win, GREEN, button_new_game)
                self.draw_text("New game", font_button, BLACK, 225, 310)
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
                if self._is_save:
                    pygame.draw.rect(self._win, GREEN, button_load_game)
                    self.draw_text("Load game", font_button, BLACK, 225, 435)
                    if click:
                        self._action = "Load"
                        run = False
            if button_new_game.collidepoint((x, y)):
                pygame.draw.rect(self._win, GREEN, button_new_game)
                self.draw_text("New game", font_button, BLACK, 225, 310)
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
                pygame.draw.rect(self._win, GREEN, button_chaos)
                self.draw_text("Chaos", font_button, BLACK, 250, 435)
                if click:
                    self._side = "Chaos"
                    run = False
            if button_order.collidepoint((x, y)):
                pygame.draw.rect(self._win, GREEN, button_order)
                self.draw_text("Order", font_button, BLACK, 250, 310)
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
                pygame.draw.rect(self._win, GREEN, button_hard)
                self.draw_text("Hard", font_button, BLACK, 260, 435)
                if click:
                    self._gamemode = "Hard"
                    run = False
            if button_easy.collidepoint((x, y)):
                pygame.draw.rect(self._win, GREEN, button_easy)
                self.draw_text("Easy", font_button, BLACK, 260, 310)
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

    def game_window_loose(self):
        run = True
        button_retry = pygame.Rect(150, 275, 300, 100)
        button_exit = pygame.Rect(150, 400, 300, 100)
        click = False
        while run:
            x, y = pygame.mouse.get_pos()
            self._win.fill(WHITE)
            font_title = pygame.font.SysFont(None, FONT_TITLE_HEADER)
            font_button = pygame.font.SysFont(None, FONT_TITLE_BUTONS)
            self.draw_text("You Lose", font_title, BLACK, 205, 100)
            pygame.draw.rect(self._win, GREY, button_retry)
            pygame.draw.rect(self._win, GREY, button_exit)
            self.draw_text("Retry", font_button, BLACK, 260, 310)
            self.draw_text("Exit", font_button, BLACK, 260, 435)
            if button_exit.collidepoint((x, y)):
                pygame.draw.rect(self._win, GREEN, button_exit)
                self.draw_text("Exit", font_button, BLACK, 260, 435)
                if click:
                    self._end_action = "Exit"
                    run = False
            if button_retry.collidepoint((x, y)):
                pygame.draw.rect(self._win, GREEN, button_retry)
                self.draw_text("Retry", font_button, BLACK, 260, 310)
                if click:
                    self._end_action = "Retry"
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


    def game_window_win(self):
        run = True
        button_retry = pygame.Rect(150, 275, 300, 100)
        button_exit = pygame.Rect(150, 400, 300, 100)
        click = False
        while run:
            x, y = pygame.mouse.get_pos()
            self._win.fill(WHITE)
            font_title = pygame.font.SysFont(None, FONT_TITLE_HEADER)
            font_button = pygame.font.SysFont(None, FONT_TITLE_BUTONS)
            self.draw_text("You Won", font_title, BLACK, 205, 100)
            pygame.draw.rect(self._win, GREY, button_retry)
            pygame.draw.rect(self._win, GREY, button_exit)
            self.draw_text("Retry", font_button, BLACK, 260, 310)
            self.draw_text("Exit", font_button, BLACK, 260, 435)
            if button_exit.collidepoint((x, y)):
                pygame.draw.rect(self._win, GREEN, button_exit)
                self.draw_text("Exit", font_button, BLACK, 260, 435)
                if click:
                    self._end_action = "Exit"
                    run = False
            if button_retry.collidepoint((x, y)):
                pygame.draw.rect(self._win, GREEN, button_retry)
                self.draw_text("Retry", font_button, BLACK, 260, 310)
                if click:
                    self._end_action = "Retry"
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