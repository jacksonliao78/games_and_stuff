
import random


class board:
    
    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end= " ")
            print()

    def first_player(self):
        return 'X' if random.randint(0, 1) == 1 else 'O'

    def switch_player(self, player):
        return 'X' if player == 'O' else 'O'

    def mark_spot(self, row, col, player):
        if self.board[row][col] != '-':
            print("This spot is already occupied.")
            return False
        else: 
            self.board[row][col] = player
            return True
        

    def is_win(self, player):
        for row in self.board:
            if row[0] == row[1] == row[2] == player:
                return True
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def is_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def start(self):

        self.create_board()
        win = False

        player = self.first_player()

        while win == False:

            print(f"Player {player}'s turn.")

            self.show_board()

            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            print()

            if self.mark_spot(row - 1, col - 1, player) == False:
                player = self.switch_player(player)

            if self.is_win(player) == True:
                win = True
                print(f"Player {player} wins!")
                break

            if self.is_filled() == True:
                win = True
                print("The game is drawn.")
                break

            player = self.switch_player(player)

        self.show_board()
        
                
a = board()
a.start()