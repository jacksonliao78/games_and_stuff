
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d9.in') as f:
    moves = f.read().split('\n')

def tailcheck(head, tail):
    if (((tail[0]-head[0])**2)+((tail[1]-head[1])**2))**0.5 >= 2:
        return True
    return False

def movetail(tail, head):
    if tail[0] == head[0]:
        if tail[1] > head[1]:
            return (tail[0], head[1]+1)
        else:   return (tail[0], head[1]-1)
    elif tail[1] == head[1]:
        if tail[0] > head[0]:
            return (head[0]+1, tail[1])
        else:   return (head[0]-1, tail[1])
    else:
        if head[0] - tail[0] == 2:
            return (head[0] - 1, head[1])
        elif head[0] - tail[0] == -2:
            return (head[0] + 1, head[1])
        elif head[1] - tail[1] == 2:
            return (head[0], head[1] - 1)
        else: return (head[0], head[1] + 1)

def switch(head, direction, amt, tail, dif):
    if direction == 'D':
        for _ in range(int(amt)):
            head = (head[0], head[1] - 1)
            if tailcheck(head, tail) == True:
                tail = movetail(tail, head)
                dif.append(tail)
        return head, tail, dif
    elif direction == 'U':
        for _ in range(int(amt)):
            head = (head[0], head[1] + 1)
            if tailcheck(head, tail) == True:
                tail = movetail(tail, head)
                dif.append(tail)
        return head, tail, dif
    elif direction == 'L':
        for _ in range(int(amt)):
            head = (head[0] - 1, head[1])
            if tailcheck(head, tail) == True:
                tail = movetail(tail, head)
                dif.append(tail)
        return head, tail, dif
    elif direction == 'R':
        for _ in range(int(amt)):
            head = (head[0] + 1, head[1])
            if tailcheck(head, tail) == True:
                tail = movetail(tail, head)
                dif.append(tail)
        return head, tail, dif


def ans():
    head = (0, 0)
    tail = (0, 0)
    dif = [(0, 0)]
    for move in moves:
        move = move.split(" ")
        head, tail, dif = switch(head, move[0], move[1], tail, dif)
    print(len(set(dif)))
    print(count)

ans() # -> 6745



