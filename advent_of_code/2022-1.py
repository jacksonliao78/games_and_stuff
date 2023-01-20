
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d1.in') as f:
    cals = f.read().split('\n')
   
def ans():
    tot = 0
    highest = 0
    for cal in cals:
        if cal == '':
            if tot > highest:
                highest = tot
            tot = 0
        else: tot += int(cal)
    print(highest)

ans()