
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d10.in') as f:
    cmds = f.read().split('\n')



def ans():
    X = 1
    cycle = 0
    tot = 0
    nc = [20, 60, 100, 140, 180, 220]
    for cmd in cmds:
        if cmd.startswith("noop"):
            cycle += 1
            if cycle in nc:
                tot += nc[nc.index(cycle)] * X
        else:
            cmd = cmd.split(" ")
            for _ in range(2):
                cycle += 1
                if cycle in nc:
                    tot += nc[nc.index(cycle)] * X
            X += int(cmd[1])
    print(tot)

ans()
            


                
