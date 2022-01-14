import pygame
from classes.game import Game
from classes.constants import SQUARE_SIZE, WIDTH, HEIGHT
from classes.window import Window


def main():
    window = Window(WIDTH, HEIGHT, "Sandbox")
    window._generate_basic_window_other_than_title("Choose Gamemode","Easy","Hard","easy","hard")


if __name__ == "__main__":
    main()
