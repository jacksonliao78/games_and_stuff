import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.board import Board
from game.pieces import Piece
from collections import deque



class Bot:

    """ Creates a new bot, with a speed cap (max pieces per second) and array of weights for the evaluation function"""
    def __init__(self, speed_cap, weights):
        self.speed_cap = speed_cap
        self.weights = {
            "height": weights[0],
            "max_height": weights[1],
            "holes": weights[2],
            "bumpiness": weights[3],
            "line_clears": weights[4],
            "well_depth": weights[5],  
            "flatness": weights[6],  
            "ds_prio": weights[7]
        }



    """ If avg height is above 15, call downstack, else call upstack """
    def stack_heights(self, board: Board):
        total = 0
        for col in range(board.width):
            highest = 0
            for row in range(board.height):
                if board.grid[row][col] != 0:
                    highest = row
                    break
            total += ( board.height - highest )
        return total / board.width

    """ Returns the best move given the list of all possible moves in a position """
    def stack(self, board, piece, queue, ds):

        vals = []
        for position in self.can_access(piece, board):
            vals.append( (self.eval_move( piece, board, position, ds ), position ) )
        
        return max(vals)

    """ Returns the highest column height of a given board state """
    def max_height(self, board):
        heights = []
        for col in range(board.width):
            highest = board.height
            for row in range(board.height):
                if board.grid[row][col] != 0:
                    highest = board.height - row
                    break
                    
            heights.append(highest)
        return max(heights)

    """ Returns the flatness of the board - the lower the standard deviation of heights, the better """
    def flatness_score(self, board):
        heights = []
        for col in range(board.width):
            highest = board.height
            for row in range(board.height):
                if board.grid[row][col] != 0:
                    highest = row
                    break
                   
            heights.append(board.height - highest)
    
        #standard deviations
        non_well_heights = heights[:9]
        avg_height = sum(non_well_heights) / len(non_well_heights)
        variance = sum( (h - avg_height) ** 2 for h in non_well_heights) / len(non_well_heights) 
    
        # Lower standard deviation = flatter surface = better score
        return -1 * (variance ** 0.5)

    """ Returns the number of cleared lines of a move """     
    def cleared_lines( self, board: Board):
        return sum( all( row ) for row in board.grid )

    """ Calculates the difference in column heights for all columns """
    def board_spikiness( self, board: Board ):

        total = 0
        heights = [0] * board.width

        for col in range( board.width ):
            for row in range( board.height ):
                if board.grid[row][col] == 1:
                    heights[col] = board.height - row
                    break
        
        for i in range(1, len(heights)):
            total += abs(heights[i] - heights[i - 1])

        return total

    """ Prioritizes building a "well" in the rightmost column """
    def well_depth(self, board):

        heights = []
        for col in range(board.width):
            highest = board.height
            for row in range(board.height):
                if board.grid[row][col] != 0:
                    highest = row
                    break
            heights.append(board.height - highest)
    
        adjacent_diff = heights[8] - heights[9]
    
        well_depth = max(0, adjacent_diff)
    
        return well_depth if well_depth >= 2 else -5
    
    """ Calculates the amount of holes in a board state - a hole being a space with a block above it """
    def get_total_holes(self, board: Board):

        total = 0

        for col in range(board.width):
            found_block = False
            for row in range(board.height):
                if board.grid[row][col] == 1:
                    found_block = True
                elif found_block and board.grid[row][col] == 0:
                    found_block = False
                    total += 1

        return total
    
    """ Evaluates a given move, considering a variety of weighted factors. 
    Higher values = better move. """
    def eval_move(self, piece: Piece, board: Board, position, ds):
       
        copy = board

        self.place_piece(piece, copy, position)

        agg_height = self.stack_heights(copy)
        max_height = self.max_height(copy)
        holes = self.get_total_holes(copy)
        bumpiness = self.board_spikiness(copy)
        line_clears = self.cleared_lines(copy)  # Implement function to check cleared lines
        well_depth = self.well_depth(copy)
        flatness = self.flatness_score(copy)

        val = (
        self.weights["height"] * agg_height * self.weights["ds_prio"] if ds else self.weights["height"] * agg_height +
        self.weights["max_height"] * max_height * 0 +
        self.weights["holes"] * holes +
        self.weights["bumpiness"] * bumpiness +
        self.weights["line_clears"] * line_clears +
        self.weights["well_depth"] * well_depth * 0 +
        self.weights["flatness"] * flatness )

        self.remove_piece(piece, copy, position)
        
        return val

    """ BFS setup """
    def can_access( self, piece: Piece, board: Board):
        
        x = int( board.width / 2 - 2) 
        y = 0
        rotation = 0
        current = (x, y, rotation)

        visited = set( (x, y, rotation) )
        cur = deque([current])

        positions = []

        return self.bfs_positions( positions, cur, piece, board, visited)

    """ Returns valid neighbors of current position """
    def get_neighbors( self, piece: Piece, board: Board, x, y, rotation ):
        directions = [(0, 1), (1, 0), (-1, 0)]
        neighbors = []
        for direction in directions:
            if piece.check_pos( board, x + direction[0], y + direction[1], rotation):
                neighbors.append((x + direction[0], y + direction[1], rotation))
        return neighbors

    """ Returns valid rotations of piece from a given position """
    def get_rotations( self, piece: Piece, board: Board, x, y, rotation ): 
        rotations = []
        for i in range( len(Piece.PIECES[ piece.type ])):
            if piece.check_pos( board, x, y, i ) :
                rotations.append( (x, y, i) )
        return rotations

    """ Uses a breadth first search (BFS) algorithm to find every reachable position on the current board """
    def bfs_positions( self, positions, queue: deque, piece: Piece, board: Board, visited: set):

        while queue:
            cur = queue.pop()
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

        return positions
        
    """ Places the piece in a position, permanently """
    def actually_place_piece( self, cur: Piece, board: Board, position):
        x, y, rotation = position
        cur.x, cur.y, cur.rotation = x, y, rotation
        cur.piece = Piece.PIECES[cur.type][cur.rotation]

        board.lock_piece(cur)

    """ Places the piece in a position, temporarily """
    def place_piece(self, cur: Piece, board: Board, position):

        x, y, rotation = position
        cur.x, cur.y, cur.rotation = x, y, rotation
        cur.piece = Piece.PIECES[cur.type][cur.rotation]

        for row_idx, row in enumerate(cur.piece):
            for col_idx, block in enumerate(row):
                if block:
                    board.grid[cur.y + row_idx][cur.x + col_idx] = 1  # Mark the grid as filled

    """ Removes a piece from a poisition, reversing place_piece """
    def remove_piece(self, cur: Piece, board: Board, position):
        
        x, y, rotation = position
        cur.x, cur.y, cur.rotation = x, y, rotation
        cur.piece = Piece.PIECES[cur.type][cur.rotation]

        for row_idx, row in enumerate(cur.piece):
            for col_idx, block in enumerate(row):
                if block:
                    board.grid[cur.y + row_idx][cur.x + col_idx] = 0

    """ Prints the current board state with '#' for filled cells and '.' for empty cells """
    def print_board(self, board: Board):
        for row in board.grid:
            print("".join("#" if cell == 1 else "O" if cell == 2 else "." for cell in row))
        print("\n" + "-" * 10)  

    """ If hold, finds the best move with the hold piece. If that move is better than the 
    best move with the current piece, use the hold piece, else use the current piece. """
    def check_hold(self, game):
        is_downstack = self.stack_heights(game.board) > 15
        
        current_val, current_pos = self.stack(game.board, game.current_tetromino, game.queue, is_downstack)
        
        if game.hold.hold_piece is None:
            second_piece = Piece( 10 // 2 - 2, 0, game.queue.check_piece(0), 250 )
            second_val, second_pos = self.stack(game.board, second_piece, game.queue, is_downstack)
            return second_val > current_val
            
        hold_piece = game.hold.hold_piece
        hold_val, hold_pos = self.stack(game.board, hold_piece, game.queue, is_downstack)
        
        return hold_val > current_val

    """ Makes a move based on what the evaluation function finds most suitable given the board state"""
    def make_move(self, game):
        
        use_hold = self.check_hold(game)
        
        if use_hold:

            game.current_tetromino = game.hold.hold(game.current_tetromino)

            if game.current_tetromino is None:
                game.current_tetromino = Piece( 10 // 2 - 2, 0, game.queue.get_piece(), 250 )



        if( self.stack_heights( game.board ) > 15 ):
            val, position = self.stack( game.board, game.current_tetromino, game.queue, True)
            self.actually_place_piece(game.current_tetromino, game.board, position)
            #prioritize clearing lines if ds? include in genetic algo
        else:
            val, position = self.stack( game.board, game.current_tetromino, game.queue, False )
            self.actually_place_piece(game.current_tetromino, game.board, position)
