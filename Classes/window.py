import pygame
from pygame.constants import K_ESCAPE, MOUSEBUTTONDOWN
from os.path import exists
from .constants import BLACK, BUTTON_1_CORDS, BUTTON_2_CORDS, BUTTON_HEIGHT, BUTTON_WIDTH, FONT_TITLE_BUTONS, FONT_TITLE_HEADER, GREEN, GREY, HEADER_CORDS, PATH, SQUARE_SIZE, WHITE, WIDTH


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

    def draw_text_auto_centered(self, text, font, color, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect(center=(WIDTH//2, y + BUTTON_HEIGHT//2))
        self._win.blit(textobj, textrect)

    def _generate_basic_window_other_than_title(self, text_title, text_button_1, text_button_2, action1, action2):
        run = True
        button_new_game = pygame.Rect(BUTTON_1_CORDS[0], BUTTON_1_CORDS[1], BUTTON_WIDTH, BUTTON_HEIGHT)
        button_load_game = pygame.Rect(BUTTON_2_CORDS[0], BUTTON_2_CORDS[1], BUTTON_WIDTH, BUTTON_HEIGHT)
        click = False
        while run:
            x, y = pygame.mouse.get_pos()
            self._win.fill(WHITE)
            font_title = pygame.font.SysFont(None, FONT_TITLE_HEADER)
            font_button = pygame.font.SysFont(None, FONT_TITLE_BUTONS)
            self.draw_text_auto_centered(f"{text_title}", font_title, BLACK, HEADER_CORDS[1])
            pygame.draw.rect(self._win, GREY, button_new_game)
            pygame.draw.rect(self._win, GREY, button_load_game)
            self.draw_text_auto_centered(f"{text_button_1}", font_button, BLACK, BUTTON_1_CORDS[1])
            self.draw_text_auto_centered(f"{text_button_2}", font_button, BLACK, BUTTON_2_CORDS[1])
            if button_load_game.collidepoint((x, y)):
                pygame.draw.rect(self._win, GREEN, button_load_game)
                self.draw_text_auto_centered(f"{text_button_2}", font_button, BLACK, BUTTON_2_CORDS[1])
                if click:
                    self._action = f"{action2}"
                    run = False
            if button_new_game.collidepoint((x, y)):
                pygame.draw.rect(self._win, GREEN, button_new_game)
                self.draw_text_auto_centered(f"{text_button_1}", font_button, BLACK, BUTTON_1_CORDS[1])
                if click:
                    self._action = f"{action1}"
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
        return self._action

    def title_screen(self):
        run = True
        button_new_game = pygame.Rect(BUTTON_1_CORDS[0], BUTTON_1_CORDS[1], BUTTON_WIDTH, BUTTON_HEIGHT)
        button_load_game = pygame.Rect(BUTTON_2_CORDS[0], BUTTON_2_CORDS[1], BUTTON_WIDTH, BUTTON_HEIGHT)
        click = False
        while run:
            x, y = pygame.mouse.get_pos()
            self._win.fill(WHITE)
            font_title = pygame.font.SysFont(None, FONT_TITLE_HEADER)
            font_button = pygame.font.SysFont(None, FONT_TITLE_BUTONS)
            self.draw_text_auto_centered("CHAOS AND ORDER", font_title, BLACK, HEADER_CORDS[1])
            pygame.draw.rect(self._win, GREY, button_new_game)
            pygame.draw.rect(self._win, GREY, button_load_game)
            self.draw_text_auto_centered("New game", font_button, BLACK, BUTTON_1_CORDS[1])
            self.draw_text_auto_centered("Load game", font_button, BLACK, BUTTON_2_CORDS[1])
            if button_load_game.collidepoint((x, y)):
                if self._is_save:
                    pygame.draw.rect(self._win, GREEN, button_load_game)
                    self.draw_text_auto_centered("Load game", font_button, BLACK, BUTTON_2_CORDS[1])
                    if click:
                        self._action = "Load"
                        run = False
            if button_new_game.collidepoint((x, y)):
                pygame.draw.rect(self._win, GREEN, button_new_game)
                self.draw_text_auto_centered("New game", font_button, BLACK, BUTTON_1_CORDS[1])
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
        action = self._generate_basic_window_other_than_title("Choose side", "Order", "Chaos", "Order", "Chaos")
        self._side = action

    def difficulty_choose_window(self):
        action = self._generate_basic_window_other_than_title("Choose difficulty", "Easy", "Hard", "Easy", "Hard")
        self._gamemode = action

    def game_window_loose(self):
        action = self._generate_basic_window_other_than_title("You Lose", "Retry", "Exit", "Retry", "Exit")
        self._end_action = action


    def game_window_win(self):
        action = self._generate_basic_window_other_than_title("You Won", "Retry", "Exit", "Retry", "Exit")
        self._end_action = action