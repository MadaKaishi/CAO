import pygame
from classes.game import Game

# Main file of the program


def main():
    game = Game()
    game.prepare_game()
    game.play()
    while game._after_action == "Retry":
        game.prepare_retry()
        game.play()
    pygame.quit()


if __name__ == "__main__":
    main()
