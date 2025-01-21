import pygame
from constants import GRID_SIZE, WHITE, RED  # Import constants



class Piece:

    PIECES = [
        # I
        [ [[1, 1, 1, 1]], [[1], [1], [1], [1]], ],
        # O
        [ [[1, 1], [1, 1]] ],
        # T 
        [ [[0, 1, 0], [1, 1, 1]], [[1, 0], [1, 1], [1, 0]], [[1, 1, 1], [0, 1, 0]], [[0, 1], [1, 1], [0, 1]]],
        # S 
        [ [[0, 1, 1], [1, 1, 0]], [[1, 0], [1, 1], [0, 1]]],
        # Z 
        [ [[1, 1, 0], [0, 1, 1]], [[0, 1], [1, 1], [1, 0]]],
        # L 
        [ [[1, 0, 0], [1, 1, 1]], [[1, 1], [1, 0], [1, 0]], [[1, 1, 1], [0, 0, 1]], [[0, 1], [0, 1], [1, 1]]],
        # J 
        [ [[0, 0, 1], [1, 1, 1]], [[1, 0], [1, 0], [1, 1]], [[1, 1, 1], [1, 0, 0]], [[1, 1], [0, 1], [0, 1]]],
    ]

    COLORS = [ ( 192, 255, 255 ), ( 255, 255, 0 ), ( 255, 192, 255 ), ( 0, 128, 0 ), (255, 0, 0), ( 0, 0, 255 ),  ( 255, 128, 0 )]

    def __init__(self, x, y, type, offset):
        self.x = x
        self.y = y
        self.type = type
        self.color = Piece.COLORS[type]
        self.piece = Piece.PIECES[type][0]
        self.rotation = 0
        self.moving = True
        self.offset = offset

    def can_move( self, board ):
        self.y += 1
        if board.is_valid_position(self):
            self.y -= 1
            return True
        self.y -= 1
        return False

    def move(self, dx, dy, board):
        if self.is_moving( board ):
            self.x += dx
            self.y += dy
            if not board.is_valid_position(self):
                self.x -= dx
                self.y -= dy
                return False
            return True
        return False

    def rotate(self, num, board):
        if(self.moving):
            self.rotation = (self.rotation + num) % len(Piece.PIECES[self.type])
            self.piece = Piece.PIECES[self.type][self.rotation]

            if not board.is_valid_position(self):
                if self.type == 0:
                    self.y -= 3
                else:
                    self.y -= 1

    def draw(self, surface):
        for row_idx, row in enumerate(self.piece):
            for col_idx, block in enumerate(row):
                if block:
                    rect = pygame.Rect(
                        (self.x + col_idx) * GRID_SIZE + self.offset,
                        (self.y + row_idx) * GRID_SIZE,
                        GRID_SIZE, GRID_SIZE
                    )
                    pygame.draw.rect(surface, self.color, rect)
                    pygame.draw.rect(surface, WHITE, rect, 1)  # Add an outline



    def hard_drop(self, board):
        while(board.is_valid_position(self)):
            self.y += 1
        self.y -= 1
        self.stop()
        

    def stop(self):
        self.moving = False

    def is_moving(self, board):
        return self.moving and board.is_valid_position(self)
    
    def get_lowest(self, board):
        pass