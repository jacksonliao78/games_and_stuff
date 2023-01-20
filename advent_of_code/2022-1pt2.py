
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d1.in') as f:
    cals = f.read().split('\n')

def ans():
    tots = []
    tot = 0
    for cal in cals:
        if cal == '':
            tots.append(tot)
            tot = 0
        else: tot += int(cal)
    tots = sorted(tots)
    print(sum(tots[-3:]))

ans()