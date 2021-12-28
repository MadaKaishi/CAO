import pygame
from gui_piece import GuiPiece
from gui_constants import SQUARE_SIZE, WIDTH, HEIGHT
from gui_board import GuiBoard


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chaos and Order")


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return int(row), int(col)


def place_circle(board, row, col):
    piece = GuiPiece(row, col, "O")
    board.place(row, col, piece)


def place_x(board, row, col):
    piece = GuiPiece(row, col, "X")
    board.place(row, col, piece)


def position_ocupied(board, row, col):
    piece = board.board()[row][col]
    if piece.symbol() == "":
        return False
    return True

def check_mouse_pos():
    pos = pygame.mouse.get_pos()
    row, col = get_row_col_from_mouse(pos)
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = GuiBoard()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                row, col = check_mouse_pos()
                if not position_ocupied(board, row, col):
                    place_x(board, row, col)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                row, col = check_mouse_pos()
                if not position_ocupied(board, row, col):
                    place_circle(board, row, col)
        board.draw(WIN)
        pygame.display.update()
        print(board.board())
    pygame.quit()


main()
