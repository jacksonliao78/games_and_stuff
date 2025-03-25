import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame
from game.constants import GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLUE  # Import constants
from game.pieces import Piece



class Board:

    SCORES = [0, 100, 300, 500, 800]
    GRAVITIES = [60, 40, 30, 22, 18, 15, 12, 10, 8, 6, 4, 2, 1]


    def __init__(self, width, height):
        self.LEVEL_LINES = [3 + 2 * i for i in range(20)]
        self.LEVEL_TOTALS = [sum(self.LEVEL_LINES[0: i]) for i in range(20)]

        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.color_grid = [[0 for _ in range(width)] for _ in range(height)]

        self.placed_pieces = 0
        self.score = 0

        self.level = 0
        self.gravity_frame = 0

        self.lines = 0
        self.combo = 0
        
    

    def is_valid_position(self, piece):

        for row_idx, row in enumerate(piece.piece):
            for col_idx, block in enumerate(row):
                if block:
                    x = piece.x + col_idx
                    y = piece.y + row_idx
                    if x < 0 or x >= self.width or y < 0 or y >= self.height or self.grid[y][x] != 0 :
                        return False
        return True

    def lock_piece(self, piece: Piece):
        for row_idx, row in enumerate(piece.piece):
            for col_idx, block in enumerate(row):
                if block:
                    x = piece.x + col_idx
                    y = piece.y + row_idx
                    self.grid[y][x] = 1
                    self.color_grid[y][x] = (1, piece.color)
        self.gravity_frame = 0
        self.placed_pieces += 1
        self.score += 5

    def clear_lines(self):
        lines = 0
        new_grid = []
        new_color_grid = [] #aa

        for i in range(len(self.grid)):  
            if all(self.grid[i]):
                lines += 1         
            else:
                new_grid.append(self.grid[i])
                new_color_grid.append(self.color_grid[i])

        for _ in range(lines):
            new_grid.insert(0, [0] * self.width)
            new_color_grid.insert(0, [0] * self.width)

        if( lines != 0 ):
            self.combo += 1
        else:
            self.combo = 0

        self.score += self.SCORES[ lines ] * self.level + self.combo * 50
        self.lines += lines
        self.update_level()
        self.grid = new_grid
        self.color_grid = new_color_grid

    def draw(self, surface, offset):
        for y, row in enumerate(self.color_grid):
            for x, block in enumerate(row):
                if block:
                    rect = pygame.Rect(
                        x * GRID_SIZE + offset,
                        y * GRID_SIZE,
                        GRID_SIZE,
                        GRID_SIZE
                    )
                    pygame.draw.rect(surface, block[1], rect)

    def draw_grid(self, surface, board_width, board_height, offset):
        for x in range(0, board_width * GRID_SIZE, GRID_SIZE):
            for y in range(GRID_SIZE, board_height * GRID_SIZE, GRID_SIZE):
                rect = pygame.Rect(x + offset, y, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(surface, WHITE, rect, 1)            

    
    def draw_score(self, surface, offset_x, offset_y):
        font = pygame.font.Font(None, 36)  

        score_text = f"Score: {self.score}"
        level_text = f"Level: {self.level}"
        lines_text = f"Lines: {self.lines}"
        combo_text = f"Combo: {self.combo}" if self.combo > 0 else ""

        score_surface = font.render(score_text, True, WHITE)
        level_surface = font.render(level_text, True, WHITE)
        lines_surface = font.render(lines_text, True, WHITE)
        combo_surface = font.render(combo_text, True, WHITE)

        score_rect = score_surface.get_rect(topleft=(offset_x, offset_y))
        level_rect = level_surface.get_rect(topleft=(offset_x, offset_y + 40))
        lines_rect = lines_surface.get_rect(topleft=(offset_x, offset_y + 80))
        combo_rect = combo_surface.get_rect(topleft=(offset_x, offset_y + 120))

        surface.blit(score_surface, score_rect)
        surface.blit(level_surface, level_rect)
        surface.blit(lines_surface, lines_rect)
        if combo_text:  
            surface.blit(combo_surface, combo_rect)


    def update_level(self):
        for i, lines in enumerate( self.LEVEL_TOTALS ):
            if self.lines > lines:
                self.level = i
        

    def gravity(self, piece: Piece):
        self.gravity_frame += 1
        if self.gravity_frame >= self.GRAVITIES[ self.level ]:
            self.gravity_frame = 0
            piece.move(0, 1, self)

    def get_score(self):
        return self.score

def test():
    board = Board(SCREEN_WIDTH, SCREEN_HEIGHT)
    print(board.LEVEL_LINES)
    print(board.LEVEL_TOTALS)

#test()