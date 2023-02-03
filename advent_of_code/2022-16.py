
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d16.in') as f:
    things = [thing for thing in f.readlines()]
    print(things)


class Solution:

    def __init__(self, info):
        self.val = 0
        self.info = info
        self.dict = {}

    def prep(self):
        pass
