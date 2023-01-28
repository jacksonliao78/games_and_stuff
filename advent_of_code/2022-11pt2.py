
import math

with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d11.in') as f:
    lines = f.read().split('\n')
    lines = [line.strip() for line in lines]


class Monkey:

    def __init__(self, lines):

        self.number = lines[0].split()[1].replace(":", "")
        self.items = [x.replace(",", "") for x in lines[1].split()[2:]]
        self.operation = lines[2].split()[-2]
        self.operand = lines[2].split()[-1]
        self.test = lines[3].split()[-1]
        self.true = lines[4].split()[-1]
        self.false = lines[5].split()[-1]
        self.inspecnum = 0

    def inspect(self, div):
        new = []
        for item in self.items:
            if self.operation == '*':
                if self.operand == 'old':
                    item = (int(item) ** 2) % div
                    new.append(item)
                    self.inspecnum += 1
                else:
                    item = (int(item) * int(self.operand)) % div
                    new.append(item)
                    self.inspecnum += 1
            elif self.operation == '-':
                item = (int(item) - int(self.operand)) % div
                new.append(item)
                self.inspecnum += 1
            elif self.operation == '+':
                item = (int(item) + int(self.operand)) % div
                new.append(item)
                self.inspecnum += 1
        self.items = new

    def tester(self, item): 
        if int(item) % int(self.test) == 0:
            return True
        return False
                
    def switch(self):
        true = []
        false = []
        for item in self.items:
            if self.tester(item) == True:
                true.append(item)
            else:
                false.append(item)
        self.items.clear()
        return true, false

    def extend(self, new):
        self.items.extend(new)

    def retnums(self):
        return self.true, self.false

    def printattributes(self):
        print(self.items)
        print(self.true)
        print(self.false)
        a, b = self.retnums()
        print(a)
        print(b)


def ans(lines):
    monkeys = []
    rnd = 0
    front, back, giganticgigathing = 0, 7, 1
    while len(lines) != 0:
        monkeys.append(Monkey(lines[front:back]))
        lines = lines[7:]
    daops = [int(monkey.test) for monkey in monkeys]
    for thing in daops:
        giganticgigathing *= thing
    while rnd != 10000:
        rnd += 1
        for monkey in monkeys:
            monkey.inspect(giganticgigathing)
            truenum, falsenum = monkey.retnums()
            true, false = monkey.switch()
            monkeys[int(truenum)].extend(true)
            monkeys[int(falsenum)].extend(false)
    vals = []
    for monkey in monkeys:
        vals.append(monkey.inspecnum)
    vals = sorted(vals)
    print(vals[-1] * vals[-2])
       

ans(lines) # -> 55216

