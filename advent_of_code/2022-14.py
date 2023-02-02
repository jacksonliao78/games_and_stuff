
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
        self.spout = (500 - min(wid), self.deepest)
        hold2 = []
        for line in self.lines:
            hold3 = []
            for lin in line:
                lin = lin.split(",")
                lin[0] = int(lin[0]) - min(wid) + 4
                hold3.append(lin)
            hold2.append(hold3)
        self.lines = hold2                

    def createboard(self):
        board = []
        for i in range(self.deepest + 3):
            row = []
            for j in range(self.widestright + 8):
                row.append(".")
            board.append(row)
        self.board = board

    def showboard(self):
        for row in self.board:
            for thing in row:
                print(thing, end = "")
            print()
        
    def makerocklines(self):
        for line in self.lines:
            for i in range(len(line) - 1):
                self.changeboard(line[i], line[i + 1])


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
        



res = Resevoir(rocks)
res.prepboard()
res.createboard()
res.makerocklines()
res.showboard()

