
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d16.in') as f:
    things = [thing.replace("Valve", "").replace("has flow rate=", "").
    replace("; tunnels lead to valves", "").
    replace("; tunnel leads to valve", "").
    strip()
    .split(" ") for thing in f.readlines()]

class Pipe:
    
    def __init__(self, stuff):
        self.val = int(stuff[1])
        self.name = stuff[0]
        self.neighbors = stuff[2:]

class Solution:

    def __init__(self, info):
        self.val = 0
        self.info = info
        self.dict = {}
        self.time = 0
        self.flowrate = 0

    def prep(self):
        for inf in self.info:
            thing = Pipe(inf)
            self.dict.update({thing.name: (thing.neighbors, thing.val)})
        

    def sol(self):
        pass

a = Solution(things)
a.prep()