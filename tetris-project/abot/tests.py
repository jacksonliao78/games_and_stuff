from bot import Bot
from game.pieces import Piece
from game.board import Board

test_avg_heights = {
    "flat_surface": [
        [0] * 10 for _ in range(15)
    ] + [
        [1] * 10 for _ in range(5)
    ],
    "staggered_surface": [
        [0] * 10 for _ in range(15)
    ] + [
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
    "one_hole": [
        [0] * 10 for _ in range(16)
    ] + [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
    "tall_column": [
        [0] * 10 for _ in range(10)
    ] + [
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0] for _ in range(10)
    ],
}



def set_board_state(board: Board, state):
 
    if len(state) != 20 or any(len(row) != 10 for row in state):
        raise ValueError("State must be a 20x10 grid.")
    board.grid = [row[:] for row in state]


def test_stack_heights():
    bot = Bot( 2 )
    board = Board(10, 20)

    for name, state in test_avg_heights.items():
        set_board_state(board, state)
        avg_height = bot.stack_heights(board)
        print(f"Test case '{name}': Average stack height = {avg_height:.2f}")

def test_positions():
    bot = Bot( 2 )
    board = Board(10, 20)

    for piece in Piece.PIECES:
        bot.get_positions(piece[0], board)

    


if __name__ == "__main__":
    #test_stack_heights()
    test_positions()
    
