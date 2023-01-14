
class yo:

    def __init__(self):
        self.height = 10
        self.width = 10
        self.board = []

    def something(self):
        for i in range(0, self.height):
            row = []
            for j in range(0, self.width):
                row.append("-")
            self.board.append(row)

    def show(self):
        for row in self.board:
            for item in row:
                print("-", end = " ")

    def start(self):
        self.something(self)
        self.show(self)

a = yo()
yo.start(yo)  

        