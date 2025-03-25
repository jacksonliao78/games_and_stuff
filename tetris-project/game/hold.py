import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame
from game.constants import GRID_SIZE, WHITE, RED  # Import constants
from game.pieces import Piece

class Hold:

    def __init__(self, offset):
        self.hold_piece = None
        self.offset = offset

    def hold(self, piece):
        if self.hold_piece != None:
            temp = self.hold_piece
            temp.x, temp.y, temp.rotation, temp.moving = 3, 0, 0, True
            temp.piece = Piece.PIECES[temp.type][temp.rotation]
            self.hold_piece = piece
            return temp
        self.hold_piece = piece
        return None

    def draw(self, surface):
        font = pygame.font.Font(None, 24)
        text = font.render("Hold:", True, WHITE)
        surface.blit(text, (10, 10))
        if self.hold_piece is not None:
            piece = Piece(0, 0, self.hold_piece.type, self.offset)
            for row_idx, row in enumerate(piece.piece):
                for col_idx, block in enumerate(row):
                    if block:
                        rect = pygame.Rect(
                            10 + col_idx * GRID_SIZE,
                            50 + row_idx * GRID_SIZE,
                            GRID_SIZE,
                            GRID_SIZE
                        )
                        pygame.draw.rect(surface, piece.color, rect)
                        pygame.draw.rect(surface, WHITE, rect, 1)


