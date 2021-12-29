import pygame
from gui.game import Game
from classes.constants import SQUARE_SIZE, WIDTH, HEIGHT

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chaos and Order")

def choose_side():
    while True:
        side = input("Choose side:\n1.Order\n2.Chaos\nPress q to quit\n")
        possible_inputs = ["1", "2"]
        if side in possible_inputs:
            break
        if side == "q":
            side = None
            break
    return side


def choose_gamemode():
    while True:
        gamemode = input("Choose gamemode:\n1.Enemy does random moves\n2.Enemy does advanced moves\nPress q to quit\n")
        possible_inputs = ["1", "2"]
        if gamemode in possible_inputs:
            break
        if gamemode == "q":
            gamemode = None
            break
    return gamemode


def main():
    side = choose_side()
    if side == "q":
        exit()
    gamemode = choose_gamemode()
    if gamemode == "q":
        exit()
    game = Game(side, gamemode, WIN)
    game.play()
    pygame.quit()


main()
