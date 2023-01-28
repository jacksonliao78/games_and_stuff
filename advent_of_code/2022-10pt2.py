
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d10.in') as f:
    cmds = f.read().split('\n')


def rw():
    row = []
    for i in range(40):
        row.append('.')
    return row


def check(cycle, register):
    if register - 1 <= cycle <= register + 1:
        return True
    return False

def update(screen, cycle):
    screen[cycle] = '#'
    return screen

def show(screen):
    for row in screen:
        for item in row:
            print(item, end = " ")
        print()



def ans():
    scr = []
    row = rw()
    X = 1
    cycle = 0
    
    for cmd in cmds:
        if cmd.startswith("noop"):
            if check(cycle, X) == True:
                row = update(row, cycle)
            cycle += 1
            if cycle == 40:
                scr.append(row)
                row = rw()
                cycle = 0

            
        else:
            cmd = cmd.split()
            for _ in range(2):
                if check(cycle, X) == True:
                    row = update(row, cycle)
                cycle += 1
                if cycle == 40:
                    scr.append(row)
                    row = rw()
                    cycle = 0
            X += int(cmd[1])

    show(scr)

ans() # -> FBURHZCH

