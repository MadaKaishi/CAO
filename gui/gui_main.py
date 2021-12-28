import pygame
from gui_constants import WIDTH, HEIGHT
from gui_board import GuiBoard


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chaos and Order")


def main():
    run = True
    clock = pygame.time.Clock()
    board = GuiBoard()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw(WIN)
        pygame.display.update()
    pygame.quit()


main()
