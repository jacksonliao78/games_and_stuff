import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame
from game.constants import GRID_SIZE, WHITE, RED  # Import constants



class Piece:

    """ Each piece, and their rotations """
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

    
    COLORS = [ ( 0, 180, 240 ), ( 240, 220, 0 ), ( 170, 0, 170 ), ( 0, 128, 0 ), (255, 0, 0), ( 0, 0, 255 ),  ( 255, 128, 0 )]
    
    """ Rotation system kicks for each piece """
    KICKS = [
    {
        (0, 1): [(0, 0), (-2, 0), (1, 0), (-2, -1), (1, 2)],
        (1, 0): [(0, 0), (2, 0), (-1, 0), (2, 1), (-1, -2)],
        (1, 2): [(0, 0), (-1, 0), (2, 0), (-1, 2), (2, -1)],
        (2, 1): [(0, 0), (1, 0), (-2, 0), (1, -2), (-2, 1)],
        (2, 3): [(0, 0), (2, 0), (-1, 0), (2, 1), (-1, -2)],
        (3, 2): [(0, 0), (-2, 0), (1, 0), (-2, -1), (1, 2)],
        (3, 0): [(0, 0), (1, 0), (-2, 0), (1, -2), (-2, 1)],
        (0, 3): [(0, 0), (-1, 0), (2, 0), (-1, 2), (2, -1)],
        (0, 2): [(0, 0), (0, 1), (0, -1)],
        (1, 3): [(0, 0), (1, 0), (-1, 0)],
        (2, 0): [(0, 0), (0, 1), (0, -1)],
        (3, 1): [(0, 0), (1, 0), (-1, 0)],
    },
    {   # O 
        (0, 1): [(0, 0)], (1, 2): [(0, 0)], (2, 3): [(0, 0)], (3, 0): [(0, 0)],
        (1, 0): [(0, 0)], (2, 1): [(0, 0)], (3, 2): [(0, 0)], (0, 3): [(0, 0)],
        (0, 2): [(0, 0)], (1, 3): [(0, 0)], (2, 0): [(0, 0)], (3, 1): [(0, 0)],
    },
    {  # T
        (0, 1): [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],
        (1, 2): [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],
        (2, 3): [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],
        (3, 0): [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],
        (1, 0): [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],
        (2, 1): [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],
        (3, 2): [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],
        (0, 3): [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],
        (0, 2): [(0, 0), (0, 1), (0, -1)],
        (1, 3): [(0, 0), (1, 0), (-1, 0)],
        (2, 0): [(0, 0), (0, 1), (0, -1)],
        (3, 1): [(0, 0), (1, 0), (-1, 0)],
    },
    {  # Z
        (0, 1): [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  
        (1, 0): [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],      
        (1, 2): [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],      
        (2, 1): [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  
        (2, 3): [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],     
        (3, 2): [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],   
        (3, 0): [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],   
        (0, 3): [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],
        (0, 2): [(0, 0), (0, 1), (0, -1)],
        (1, 3): [(0, 0), (1, 0), (-1, 0)],
        (2, 0): [(0, 0), (0, 1), (0, -1)],
        (3, 1): [(0, 0), (1, 0), (-1, 0)],
    },
    {  # S
        (0, 1): [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  
        (1, 0): [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],      
        (1, 2): [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],      
        (2, 1): [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  
        (2, 3): [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],     
        (3, 2): [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],   
        (3, 0): [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],   
        (0, 3): [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],
        (0, 2): [(0, 0), (0, 1), (0, -1)],
        (1, 3): [(0, 0), (1, 0), (-1, 0)],
        (2, 0): [(0, 0), (0, 1), (0, -1)],
        (3, 1): [(0, 0), (1, 0), (-1, 0)],
    },
    { # L
        (0, 1): [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  
        (1, 0): [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],      
        (1, 2): [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],      
        (2, 1): [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  
        (2, 3): [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],     
        (3, 2): [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],   
        (3, 0): [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],   
        (0, 3): [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],
        (0, 2): [(0, 0), (0, 1), (0, -1)],
        (1, 3): [(0, 0), (1, 0), (-1, 0)],
        (2, 0): [(0, 0), (0, 1), (0, -1)],
        (3, 1): [(0, 0), (1, 0), (-1, 0)],
    },
    {  # J
        (0, 1): [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  
        (1, 0): [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],      
        (1, 2): [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],      
        (2, 1): [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  
        (2, 3): [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],     
        (3, 2): [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],   
        (3, 0): [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],   
        (0, 3): [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],
        (0, 2): [(0, 0), (0, 1), (0, -1)],
        (1, 3): [(0, 0), (1, 0), (-1, 0)],
        (2, 0): [(0, 0), (0, 1), (0, -1)],
        (3, 1): [(0, 0), (1, 0), (-1, 0)],
    },
    ]

    """ Initilizes a piece, given a type """
    def __init__(self, x, y, type, offset):
        self.x = x
        self.y = y
        self.type = type
        self.color = Piece.COLORS[type]
        self.rotation = 0
        self.piece = Piece.PIECES[type][self.rotation]
        self.moving = True
        self.offset = offset
        self.lowest = 0

    """ Checks if a piece can move downwards """
    def can_move( self, board):
        self.y += 1
        if board.is_valid_position( self ):
            self.y -= 1
            return True
        self.y -= 1
        return False

    """ Checks if a piece can move downwards at a specific position """
    def can_move_2( self, board, position ):
        old_rotation = self.rotation
        old_x = self.x
        old_y = self.y
        self.rotation = position[2]
        self.x = position[0]
        self.y = position[1]
        self.piece = Piece.PIECES[self.type][self.rotation]

        if self.can_move( board ):
            self.rotation = old_rotation
            self.x = old_x
            self.y = old_y
            self.piece = Piece.PIECES[self.type][self.rotation]

            return True
        self.rotation = old_rotation
        self.x = old_x
        self.y = old_y
        self.piece = Piece.PIECES[self.type][self.rotation]

        return False

    """ Moves a piece down once if possible """
    def move(self, dx, dy, board):
        self.get_lowest(board)
        if self.is_moving( board ):
            self.x += dx
            self.y += dy
            if not board.is_valid_position(self):
                self.x -= dx
                self.y -= dy
                return False
            return True
        return False

    """ Attempts to rotate a piece using the kick system or normal rotation """
    def rotate(self, num, board):
        if(self.moving):
            old_rotation = self.rotation
            self.rotation = (self.rotation + num) % len(Piece.PIECES[self.type])
            self.piece = Piece.PIECES[self.type][self.rotation]
        
            if board.is_valid_position(self):
                return
        
            kicks = Piece.KICKS[self.type][(old_rotation, self.rotation)]

            for dx, dy in kicks:
                self.x += dx
                self.y += dy
                if board.is_valid_position(self):
                    return
                self.x -= dx
                self.y -= dy

            self.rotation = old_rotation
            self.piece = Piece.PIECES[self.type][self.rotation]

    """ Draws the piece, and a ghost version at the lowest point """
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
        for row_idx, row in enumerate(self.piece):
            for col_idx, block in enumerate(row):
                if block:
                    rect = pygame.Rect(
                        (self.x + col_idx) * GRID_SIZE + self.offset,
                        (self.lowest + row_idx) * GRID_SIZE,
                        GRID_SIZE, GRID_SIZE
                    )
                    pygame.draw.rect(surface, (*self.color, 40) ,rect) #need a lighter version ot
                    pygame.draw.rect(surface, WHITE, rect, 1)

    """ Moves the piece down as far as possible """
    def hard_drop(self, board):
        while(board.is_valid_position(self)):
            self.y += 1
        self.y -= 1
        self.stop()

    """ Stops piece movement """
    def stop(self):
        self.moving = False

    """ Returns whether the piece is moving """
    def is_moving(self, board):
        return self.moving and board.is_valid_position(self)
    
    """ Essentially can_move_2 but with the position unpacked """
    def check_pos( self, board, x, y, rotation ):
        old_rotation = self.rotation
        old_x = self.x
        old_y = self.y        
        self.rotation = rotation
        self.x = x
        self.y = y

        self.piece = Piece.PIECES[self.type][self.rotation]
        if board.is_valid_position(self): #add second requirement for peice to stop
            self.x = old_x
            self.y = old_y
            self.rotation = old_rotation
            self.piece = Piece.PIECES[self.type][self.rotation]
            return True
        self.x = old_x
        self.y = old_y
        self.rotation = old_rotation
        self.piece = Piece.PIECES[self.type][self.rotation]

        return False        
    
    """ Finds the lowest valid positon for a piece"""
    def get_lowest(self, board): 
        old_y = self.y
        while(board.is_valid_position(self)):
            self.y += 1
        self.y -= 1
        self.lowest = self.y
        self.y = old_y