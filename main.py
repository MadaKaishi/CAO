import pygame
from classes.game import Game


def main():
    game = Game()
    game.prepare_game()
    game.play()
    pygame.quit()


if __name__ == "__main__":
    main()
