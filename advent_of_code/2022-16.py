
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d16.in') as f:
    things = [thing.replace("Valve", "").replace("has flow rate=", "").
    replace("; tunnels lead to valves", "").
    replace("; tunnel leads to valve", "").
    replace(",", "").
    strip()
    .split(" ") for thing in f.readlines()]

class Pipe:
    
    def __init__(self, stuff):
        self.val = int(stuff[1])
        self.name = stuff[0]
        self.neighbors = stuff[2:]
        self.visited = False

class Solution:

    def __init__(self, info):
        self.val = 0
        self.info = info
        self.dict = {}
        self.time = 0
        self.flowrate = 0
        self.pipe = "AP"

    def prep(self):
        for inf in self.info:
            thing = Pipe(inf)
            self.dict.update({thing.name: [thing.neighbors, thing.val, thing.visited]})  

    def best(self, pipe):
        vals = []
        neighbors = []
        for thing in self.dict[pipe][0]:
            if self.dict[thing][2] == False:
                vals.append(self.dict[thing][1])
                neighbors.append(thing)
            elif len(self.dict[pipe][0]) == 1:
                return 1, thing
        if len(vals) >= 1:
            self.flowrate += max(vals)
            return 2, neighbors[vals.index(max(vals))]
        else:
            return 1, self.dict[pipe][0][0]

    def sol(self):
        pipe = self.pipe
        while self.time != 30:
            self.time += 1
            self.val += self.flowrate
            a, pipe = self.best(pipe)
            print(self.flowrate)
            self.dict[pipe][2] = True
            if a == 1:
                continue
            else:
                self.time += 1
                self.val += self.flowrate
        print(self.val)
            
            
            
#469 low what a surprise D:


a = Solution(things)
a.prep()
a.sol()