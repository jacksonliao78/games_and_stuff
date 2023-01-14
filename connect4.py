
class board:

    def __init__(self):
        self.board = []

    def new_board(self):
        for i in range(6):
            row = []
            for i in range(7):
                row.append("-")
            self.board.append(row)
        self.board.append(['*', '*', '*', '*', '*', '*', '*'])
        self.board.append(['1', '2', '3', '4', '5', '6', '7'])

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end = " ")
            print()

    def switch_player(self, player):
        return '1' if player == '2' else '2'

    def mark_spot(self, col, player):
        i = 6
        while True:
            i -= 1
            if self.board[i][col] != '-':
                pass
            else:
                self.board[i][col] = player
                break

    def is_win(self, player):
        for i in range(7):
            for j in range(4):
                if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3] == player:
                    return True
        for i in range(7):
            for j in range(3):
                if self.board[j][i] == self.board[j + 1][i] == self.board[j + 2][i] == self.board[j + 3][i] == player:
                    return True
        for i in range(3):
            for j in range(4):
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] == player:
                    return True
        for i in range(3):
            for j in range(4):
                if self.board[i][6 - j] == self.board[i + 1][5 - j] == self.board[i + 2][4 - j] == self.board[i + 3][3 - j] == player:
                    return True
        return False

    def is_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def start(self):
        win = False

        player = '1'
        self.new_board()
        self.show_board()

        while win == False:
            print()
            print(f"Player {player}'s turn.")
            
            col = int(input("Enter a column: "))
            print()

            self.mark_spot(col - 1, player)

            if self.is_win(player) == True:
                print(f"Player {player} wins!")
                self.show_board()
                win = True
                break
            
            if self.is_filled == True:
                print("The game is drawn.")
                win = True
                break

            self.show_board()

            player = self.switch_player(player)



a = board()
a.start()

