import sys
import os
from collections import deque

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
    """Sets the board state for testing."""
    if len(state) != 20 or any(len(row) != 10 for row in state):
        raise ValueError("State must be a 20x10 grid.")
    board.grid = [row[:] for row in state]


def test_stack_heights():
    """Tests stack height calculations."""
    bot = Bot(2)
    board = Board(10, 20)

    print("\n--- Testing Stack Heights ---")
    for name, state in test_avg_heights.items():
        set_board_state(board, state)
        avg_height = bot.stack_heights(board)
        print(f"Test case '{name}': Average stack height = {avg_height:.2f}")


def test_positions():
    """Tests piece placements."""
    bot = Bot(2)
    board = Board(10, 20)

    board.grid[18][4] = 1
    board.grid[17][4] = 1
    board.grid[16][5] = 1



def test_bfs():
    """Tests BFS-based reachable positions."""
    bot = Bot(2)
    board = Board(10, 20)

    # Create obstacles
    board.grid[18][4] = 2
    board.grid[17][4] = 2
    board.grid[16][5] = 2

    

    #x-y 4,18 4,17, 5,16
    piece = Piece( 5, 0, 0, 0)

    print(bot.get_positions(piece, board))
    # Place an "I" piece at the top
    for i in range(1):
        piece = Piece( 5, 0, i, 0)
        print("skibidi bruh")
        for pos in sorted(bot.can_access( piece, board )):
            
            bot.place_piece( piece, board, pos )
            bot.print_board(board)
            bot.remove_piece( piece, board, pos )
            
        print("-" * 30)


    # Run BFS to find accessible positions



if __name__ == "__main__":
    test_stack_heights()
    test_positions()
    test_bfs()
