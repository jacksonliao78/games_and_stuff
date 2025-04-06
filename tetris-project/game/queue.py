import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame
import random
from game.constants import GRID_SIZE, SCREEN_WIDTH, WHITE, BLUE  # Import constants
from game.pieces import Piece

class Queue:

    """ Initiates a queue """
    def __init__(self, offset):
        self.offset = offset
        self.bag = []
        self.queue = []
        self.generate_bag(1)
        for _ in range(5):
            self.queue.append(self.bag.pop())

    """ Generates a pseudo-randomized bag """
    def generate_bag(self, times):
        self.bag = []
        for _ in range(times):
            new_bag = list(range(7))
            random.shuffle(new_bag)
            self.bag.extend(new_bag)

    """ Returns the piece at the top of the queue """
    def get_piece(self):
        if len(self.bag) == 0:
            self.generate_bag(2)
        self.queue.append(self.bag.pop())
        return self.queue.pop(0)
    
    """ Checks what piece is in the nth index of the queue """
    def check_piece(self, num):
        if num >= len(self.queue):
            return None
        return self.queue[num]

    """ Draws the queue """
    def draw(self, surface):
        font = pygame.font.Font(None, 24)
        text = font.render("Next:", True, WHITE)
        surface.blit(text, (SCREEN_WIDTH + self.offset, 10)) 
        for i, piece_type in enumerate(self.queue):
            piece = Piece(0, 0, piece_type, self.offset)
            for row_idx, row in enumerate(piece.piece):
                for col_idx, block in enumerate(row):
                    if block:
                        rect = pygame.Rect(
                            SCREEN_WIDTH + self.offset + col_idx * GRID_SIZE,
                            50 + i * 4 * GRID_SIZE + row_idx * GRID_SIZE,
                            GRID_SIZE,
                            GRID_SIZE
                        )
                        pygame.draw.rect(surface, piece.color, rect)
                        pygame.draw.rect(surface, WHITE, rect, 1)