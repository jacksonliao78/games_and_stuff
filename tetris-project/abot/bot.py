from game.board import Board
from game.pieces import Piece


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
        pass

    def upstack(self, board, piece, queue):
        pass


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

    def eval_position(self, piece, board):
        pass

    def get_positions(self, piece: Piece, board ):

        for pos in Piece.PIECES[piece.type]:
            print(pos)

        pass

    def can_access( self, piece, board, position ):
        return False

    def place_piece( self, piece, board, position ):
        pass

def test():
    a = Bot( 2 )
    board = Board( 20, 20 )

    print(a.stack_heights( board ))

if __name__ == "__main__":
    test()