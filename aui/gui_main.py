import os
import pygame
from gui_constants import WIDTH, HEIGHT

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chaos and Order")
os.environ["SDL_VIDEODRIVER"]="x11"

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    pygame.quit()


main()
