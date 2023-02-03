
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d14.in') as f:
    rocks = [(row.strip()) for row in f.readlines()]

class Resevoir:
    
    def __init__(self, rocklines):
        self.lines = rocklines
        self.deepest = 0
        self.widestleft = 0
        self.widestright = 0
        self.spout = (500, 0)
        self.board = []
        self.total = 0

    def prepboard(self):
        hold = []
        yep = []
        wid = []
        for line in self.lines:
            line = [thing.strip() for thing in line.split("->")]
            hold.append(line)
            for lin in line:
                lin = lin.split(",")
                yep.append(int(lin[1]))
                wid.append(int(lin[0]))
        self.lines = hold
        self.deepest = max(yep)
        self.widestright = max(wid) - min(wid)
        self.spout = (500 - min(wid) + 200, 0)
        hold2 = []
        for line in self.lines:
            hold3 = []
            for lin in line:
                lin = lin.split(",")
                lin[0] = int(lin[0]) - min(wid) + 200
                hold3.append(lin)
            hold2.append(hold3)
        self.lines = hold2                

    def createboard(self):
        board = []
        for i in range(self.deepest + 3):
            row = []
            for j in range(self.widestright + 400):
                row.append(".")
            board.append(row)
        self.board = board
        self.board[self.spout[1]][self.spout[0]] = "+"

    def showboard(self):
        for row in self.board:
            for thing in row:
                print(thing, end = "")
            print()
        print(self.total)
        
    def makerocklines(self):
        for line in self.lines:
            for i in range(len(line) - 1):
                self.changeboard(line[i], line[i + 1])
        for i in range(len(self.board[-1])):
            self.board[-1][i] = "#"
            


    def changeboard(self, beg, end):
        beg, end = [beg[0], int(beg[1])], [end[0], int(end[1])]
        if beg[0] == end[0]:
            if beg[1] > end[1]:
                for i in range(int(end[1]), int(beg[1]) + 1):
                    self.board[i][beg[0]] = '#'
            else:
                for i in range(int(beg[1]), int(end[1]) + 1):
                    self.board[i][beg[0]] = '#'
        elif beg[1] == end[1]:
            if beg[0] > end[0]:
                for i in range(int(end[0]), int(beg[0]) + 1):
                    self.board[beg[1]][i] = '#'
            else:
                for i in range(int(beg[0]), int(end[0]) + 1):
                    self.board[beg[1]][i] = '#'

    def checkpos(self, cords):
        if self.board[cords[0]][cords[1]] == '+':
            return False
        return True

    def update(self, coords):
        while True:
            if self.board[coords[0] + 1][coords[1]] == ".":
                coords = ((coords[0] + 1), coords[1])
            elif self.board[coords[0] + 1][coords[1] - 1] == ".":
                coords = ((coords[0] + 1), coords[1] - 1)
            elif self.board[coords[0] + 1][coords[1] + 1] == ".":
                coords = ((coords[0] + 1), coords[1] + 1)
            else:
                break
        if self.checkpos(coords) == True:
            self.board[coords[0]][coords[1]] = 'o'
            return True
        else:
            return False
    
    def sand(self):
        res.prepboard()
        res.createboard()
        res.makerocklines()
        #we want the y val first if this is a graph
        while  True:
            if self.update((0, self.spout[0])) == True:
                self.total += 1
            else:
                break
        print(self.total + 1)
        
res = Resevoir(rocks)
res.sand()
res.showboard()

