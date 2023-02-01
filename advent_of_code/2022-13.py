
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d13.in') as f:
    thing = [list(row.strip()) for row in f.readlines()]

def compare(left, right):
    while len(left) > 0 and len(right) > 0:
        lef, rig = left.pop(0), right.pop(0)
        if type(lef) == type(rig) == int:
            if lef < rig:
                return 1
            elif lef > rig:
                return -1
        if type(lef) == type(rig) == list:
            comp = compare(lef, right)
            if comp != 0:
                return comp
        if type(lef) == int and type(rig) == list:
            comp = compare(list(lef), rig)
            if comp != 0:
                return comp
        if type(lef) == list and type(rig) == int:
            comp = compare(lef, list(rig))
            if comp != 0:
                return comp
    if len(left) > len(right):
        return -1
    elif len(left) < len(right):
        return 1
    else:
        return 0

def ans(things):
    index = 1
    tot = 0
    print(len(things))
    print(things)
    while len(things) != 0:
        num = compare(things[0], things[1])
        print(things[0], things[1])
        things = things[3:]
        if num == 1:
            tot += index
        index += 1
    print(tot)

#ans(thing) #5571 too low

with open('/Users/jliao/Code/games_and_stuff/advent_of_code/test.in') as b:
    thing2 = [list(row.strip()) for row in b.readlines()]

ans(thing2)