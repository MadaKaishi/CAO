import pygame
from classes.game import Game
from classes.constants import SQUARE_SIZE, WIDTH, HEIGHT
from classes.window import Window

FPS = 60


def main():
    game = Game()
    game.prepare_game()
    game.play()
    pygame.quit()


main()
