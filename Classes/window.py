import pygame
from typing import Union
from pygame.constants import K_ESCAPE, MOUSEBUTTONDOWN
from os.path import exists
from .constants import BLACK, BUTTON_1_CORDS, BUTTON_2_CORDS, BUTTON_HEIGHT, \
    BUTTON_WIDTH, FONT_TITLE_BUTONS, FONT_TITLE_HEADER, GREEN, GREY, \
    HEADER_CORDS, PATH, SQUARE_SIZE, WHITE, WIDTH


class Window:
    """Class Window:
    This class represents window that is displayed to user of program.
    User can communicate with programs in certain situations using buttons
    and interacting with them using mouse
    """
    def __init__(self, width: int, height: int, caption: str):
        """
        Initializes the Window object
        Width and height represents width and height of the window.
        Caption defines name of window
        Side, gamemode, action, game_end_action and save are set to None
        """
        pygame.init()
        # set window size to (width, height)
        self._win = pygame.display.set_mode((width, height))
        # set name of window
        pygame.display.set_caption(f"{caption}")
        # set variables to none
        self._side = None
        self._gamemode = None
        self._action = None
        self._end_action = None
        self._is_save = None
        self.check_save()  # check if save file exist

    def end_action(self) -> Union[str, None]:
        """Returns self._end_action"""
        return self._end_action

    def side(self) -> Union[str, None]:
        """Returns self._side"""
        return self._side

    def gamemode(self) -> Union[str, None]:
        """Returnes self._gamemode"""
        return self._gamemode

    def action(self) -> Union[str, None]:
        """Returnes self._action"""
        return self._action

    def win(self) -> "Window":
        """Returnes self._win"""
        return self._win

    def check_save(self):
        """Returnes True is save file exist"""
        if exists(f"{PATH}"):
            self._is_save = True
        else:
            self._is_save = False

    def check_mouse_pos(self) -> tuple:
        """Returnes row and column based od mouse position on board"""
        pos = pygame.mouse.get_pos()
        row, col = self.get_row_col_from_mouse(pos)
        return row, col

    def get_row_col_from_mouse(self, pos: tuple) -> tuple:
        """Calculates row and column based on mouse position"""
        x, y = pos
        row = y//SQUARE_SIZE
        col = x//SQUARE_SIZE
        return int(row), int(col)

    def update(self):
        """Updates window"""
        pygame.display.update()

    def draw_text(self, text: int, font: int, color: tuple, x: int, y: int):
        """Draws text inside the rectangle"""
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self._win.blit(textobj, textrect)

    def draw_text_auto_centered(self, text: str, font: int,
                                color: tuple, y: int):
        """Draws rectangle with text that is auto centered"""
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect(center=(WIDTH//2, y + BUTTON_HEIGHT//2))
        self._win.blit(textobj, textrect)

    def _generate_basic_window(self, text_title: str, text_button_1: str,
                               text_button_2: str, action1: str,
                               action2: str) -> str:
        """
        Generates basic window with parameters equal to given as arguments
        Basic window consist of:\n
        Header Caption (text_title)
        Upper button with text (text_button_1)
        Bottom button with text (text_button_2)
        Acction connected to button_1
        Acction connected to button_2
        Method returnes action player have chosen
        """
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
                    action = f"{action2}"
                    run = False
            if button_new_game.collidepoint((x, y)):
                pygame.draw.rect(self._win, GREEN, button_new_game)
                self.draw_text_auto_centered(f"{text_button_1}", font_button, BLACK, BUTTON_1_CORDS[1])
                if click:
                    action = f"{action1}"
                    run = False
            self.update()
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # if user leaves the game
                    action = None
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:  # if escape key is pressed
                    if event.key == K_ESCAPE:
                        action = None
                        run = False
                        pygame.quit()
                if event.type == MOUSEBUTTONDOWN:  # if left clik is presses
                    if event.button == 1:
                        click = True
        return action

    def title_screen(self):
        """
        Generates title screen of game, its functions differ from
        this of basic windows, for example, when save file is not present
        Load Game button is unachivable for user to click, blocking him
        from loading empty game
        """
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
                if self._is_save:  # when save file is present
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
                if event.type == pygame.QUIT:  # if game is closed
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:  # if escape is pressed
                    if event.key == K_ESCAPE:
                        run = False
                        pygame.quit()
                if event.type == MOUSEBUTTONDOWN:  # if left button is clicked
                    if event.button == 1:
                        click = True

    def side_choose_window(self):
        """Generates side choose window, appends self._action attribute"""
        action = self._generate_basic_window("Choose side", "Order",
                                             "Chaos", "Order", "Chaos")
        self._side = action

    def difficulty_choose_window(self):
        """Generates difficulty choose widnow,
        appends self._gamemode attrubite"""
        action = self._generate_basic_window("Choose difficulty", "Easy",
                                             "Hard", "Easy", "Hard")
        self._gamemode = action

    def game_window_lose(self):
        """Generates window displaying that player have lost,
        appends self._end_action attribute (Exit or Retry)"""
        action = self._generate_basic_window("You Lose", "Retry",
                                             "Exit", "Retry", "Exit")
        self._end_action = action

    def game_window_win(self):
        """Generates window displaying that player have won,
        appends self._end_action attribute (Exit or Retry)"""
        action = self._generate_basic_window("You Won", "Retry",
                                             "Exit", "Retry", "Exit")
        self._end_action = action
