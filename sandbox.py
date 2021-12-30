import pygame
from classes.game import Game
from classes.constants import SQUARE_SIZE, WIDTH, HEIGHT
from classes.window import Window


def main():
    window = Window(WIDTH, HEIGHT, "Sandbox")
    window.title_screen()
    if window.action() == "New":
        window.side_choose_window()
        window.difficulty_choose_window()
    if window.action() == "Load":
        window.game_window_loose()
        window.game_window_win()


if __name__ == "__main__":
    main()
