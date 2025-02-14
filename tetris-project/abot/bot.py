import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.board import Board
from game.pieces import Piece
from game.main import Game
from collections import deque


#TODO - everything ->
#start with quad spam?

#with i piece should check if quad is possible...



class Bot:

    def __init__(self, speed_cap):
        self.speed_cap = speed_cap
        self.weights = {
            "aggregate_height": -0.5,
            "holes": -1.0,
            "bumpiness": -0.4,
            "line_clears": 1.5,
            "well_depth": 0.8,  
            "blocked_well": -2.0,  
        }


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
            vals.append(self.eval_move( position ), position)
        
        return max(vals)


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
            
    def cleared_lines( self, board: Board):
        return sum( all( row ) for row in board.grid )


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

    def open_well( self, board ):
        well_open = all(board.grid[row][9] == 0 for row in range(20))
        return 100 if well_open else -100

    def get_total_holes( self, board: Board ):
        total = 0

        for i in range(board.width):
            for j in range(board.height - 1, 0, -1):
                if( board.grid[j + 1][i] == 1 and board.grid[j + 1][i] == 0):
                    total += 1

        return total

    def eval_move(self, piece: Piece, board: Board, position):

        copy = board.copy()

        self.place_piece(piece, copy, position)

        agg_height = self.stack_heights(copy)
        holes = self.get_total_holes(copy)
        bumpiness = self.board_spikiness(copy)
        line_clears = copy.get_line_clears()  # Implement function to check cleared lines
        well_depth = self.well_depth(copy)
        blocked_well = self.blocked_well(copy)

        val = (
        self.weights["aggregate_height"] * agg_height +
        self.weights["holes"] * holes +
        self.weights["bumpiness"] * bumpiness +
        self.weights["line_clears"] * line_clears +
        self.weights["well_depth"] * well_depth +
        self.weights["blocked_well"] * blocked_well )

        self.remove_piece(piece, copy, position)
        
        return val

    

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

        return self.bfs_positions( positions, cur, piece, board, visited)

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
            #print(queue)

        return positions
        
    

    def place_piece(self, cur: Piece, board: Board, position):
        """
        Places a piece on the board at the given position.
        Assumes `position` is a tuple (x, y, rotation).
        """

        print(position)

        x, y, rotation = position
        cur.x, cur.y, cur.rotation = x, y, rotation
        cur.piece = Piece.PIECES[cur.type][cur.rotation]


        for row_idx, row in enumerate(cur.piece):
            for col_idx, block in enumerate(row):
                if block:
                    print( cur.y + row_idx, cur.x + col_idx )
                    board.grid[cur.y + row_idx][cur.x + col_idx] = 1  # Mark the grid as filled


    def remove_piece(self, cur: Piece, board: Board, position):
        """
        Removes a piece from the board at the given position.
        Assumes `position` is a tuple (x, y, rotation).
        """
        x, y, rotation = position
        cur.x, cur.y, cur.rotation = x, y, rotation
        cur.piece = Piece.PIECES[cur.type][cur.rotation]


        for row_idx, row in enumerate(cur.piece):
            for col_idx, block in enumerate(row):
                if block:
                    board.grid[cur.y + row_idx][cur.x + col_idx] = 0


    def print_board(self, board: Board):
        """
        Prints the current board state with '#' for filled cells and '.' for empty cells.
        """
        for row in board.grid:
            print("".join("#" if cell == 1 else "O" if cell == 2 else "." for cell in row))
        print("\n" + "-" * 10)  


    def main(self):

        game = Game()
        pass

def test():
    a = Bot( 2 )
    board = Board( 20, 20 )

    print(a.stack_heights( board ))

if __name__ == "__main__":
    test()