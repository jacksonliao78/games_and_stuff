
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d7.in') as f:
    cmds = f.read().split('\n')

from collections import defaultdict

def ans():
    a = defaultdict(int)
    path = []

    for cmd in cmds:
        if cmd.startswith("$ cd"):
            if cmd == '$ cd /':
                path.clear()
                path.append("/")
            elif cmd == '$ cd ..':
                path.pop()
            else:
                dire = cmd.split()[-1]
                path.append(dire)
        else:
            size = (cmd.split()[0])
            if size.isdigit():
                size = int(size)
                for i in range(len(path)):
                    dire = '/'.join(path[:i + 1]).replace("//", "/")
                    a[dire] += size
    return a

def solve():
    a = ans()
    tot = 0
    for dire in a:
        if a[dire] <= 100000:
            tot += a[dire]
    print(tot)




solve()