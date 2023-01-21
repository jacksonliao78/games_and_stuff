
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d4.in') as f:
    pairs = f.read().split('\n')

def contain(pair):
    things = pair.split(",")
    things2 = []
    for thing in things:
        things2.append(thing.split("-"))
    if int(things2[0][0]) >= int(things2[1][0]) and int(things2[0][1]) <= int(things2[1][1]) or int(things2[0][0]) <= int(things2[1][0]) and int(things2[0][1]) >= int(things2[1][1]):
        return True
    return False

def ans():
    count = 0
    for pair in pairs:
        if contain(pair) == True:
            count += 1
    print(count)

ans()



