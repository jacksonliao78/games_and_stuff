import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.board import Board
from game.pieces import Piece
from collections import deque


#TODO - everything ->
#start with quad spam?

#with i piece should check if quad is possible...



class Bot:

    def __init__(self, speed_cap):
        self.speed_cap = speed_cap


    """ if avg height is above 15, call downstack, else call upstack"""
    def stack_heights(self, board: Board):
        total = 0
        for i in range(board.width):
            highest = 0
            for j in range(board.height):
                if board.grid[j][i] != 0:
                    highest = max(highest, i)
            total += highest
        return total / board.width

    def evaluate_board(self, board: Board, piece: Piece, queue):

        if piece.type == 0:
            pos = self.quad( board )
            if pos == 1:
                self.upstack()
            

        if( self.stack_heights( board ) > 15 ):
            self.downstack()
        else:
            self.upstack()
        
        #figure out how to see how tall the stack is 

        pass

    

    def downstack(self, board, piece, queue):
        vals = []

    def upstack(self, board, piece, queue):
        vals = []
        for position in self.can_access(piece, board):
            self.eval_move( position )


    def quad(self, board: Board):
        curr = -1
        curr_hole = -1
        consecutive = 0
 
        for i in range(board.height):
            tot = 0
            hole = -1
            for j in range(board.width):
                if board.grid[i][j] == 1:
                    tot += 1
                else:
                    hole = j
            if tot == board.width - 1:
                if curr - i == 1 and curr_hole == hole:
                    consecutive += 1
                else:
                    consecutive = 1
                curr = i
            if consecutive >= 4 and i + 1 == board.height or board.grid[i + 1][curr_hole] == 1:
                return curr

    def board_spikiness( self, board: Board ):

        total = 0

        heights = [0] * board.width

        for i in range( board.width ):
            for j in range( board.height ):
                if board.grid[j][i] == 1:
                    heights[i] == board.height - j
                    break
        
        for i in range(1, len(heights)):
            total += abs(heights[i] - heights[i - 1])

        return total

    def holes( self, board: Board ):
        pass

    def eval_move(self, piece: Piece, board: Board):
        val = 0
        pass

    
    def eval_move(self, piece: Piece, board: Board):
        val = 0
        pass

    def get_positions(self, piece: Piece, board: Board ):

        positions = []

        for i in range(len(Piece.PIECES[piece.type])):
            piece.rotation = i

            for x in range( -2, board.width):
                piece.x = x
                piece.y = 0

                while piece.y >= board.height:
                    if( board.is_valid_position( piece ) and board.grid[x][piece.y + 1] == 1 or piece.y == board.height ):
                        positions.append( x, piece.y, i)
                
        return positions

    def can_access( self, piece: Piece, board: Board):
        
        x = int(board.width / 2)
        y = 0
        rotation = 0
        current = (x, y, rotation)

        visited = set( (x, y, rotation) )
        cur = deque([current])

        positions = []

        #use bfs to find possible places? probably better than get_positions
        
        return self.bfs_positions( positions, cur, piece, board, visited)


        #if piece.can_move( board )

      
    
        # use rotations / slimmest side? i.e. straight I then rotate long way

    def get_neighbors( self, piece: Piece, board: Board, x, y, rotation ):
        directions = [(0, 1), (1, 0), (-1, 0)]
        neighbors = []
        for direction in directions:
            if piece.check_pos( board, x + direction[0], y + direction[1], rotation):
                neighbors.append((x + direction[0], y + direction[1], rotation))
        return neighbors

    def get_rotations( self, piece: Piece, board: Board, x, y, rotation ):
        rotations = []
        for i in range( len(Piece.PIECES[ piece.type ])):
            if piece.check_pos( board, x, y, i ) :
                rotations.append( (x, y, i) )
        return rotations

    def bfs_positions( self, positions, queue: deque, piece: Piece, board: Board, visited: set):

        while queue:
            cur = queue.pop()
            print(cur)
            if( not piece.can_move_2( board, cur ) ): 
                positions.append( cur )
            for neighbor in self.get_neighbors( piece, board, cur[0], cur[1], cur[2] ):
                if neighbor not in visited:
                    queue.append( neighbor )
                    visited.add( neighbor )
            for rotation in self.get_rotations( piece, board, cur[0], cur[1], cur[2] ):
                if rotation not in visited:
                    queue.append( rotation )
                    visited.add( rotation  )
            print(queue)

        return positions
        
    

    def place_piece( self, piece, board, position ):
        pass

def test():
    a = Bot( 2 )
    board = Board( 20, 20 )

    print(a.stack_heights( board ))

if __name__ == "__main__":
    test()