
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d9.in') as f:
    moves = f.read().split('\n')

def visited(cord, unique):
    for thing in unique:
        if cord == unique:
            return True
    return False

def tailcheck(head, tail):
    if (((tail[0]-head[0])**2)+((tail[1]-head[1])**2))**0.5 >= 2:
        return True
    return False

def switch(head, direction, amt, tail):
    if direction == 'D':
        for _ in range(amt):
            head = (head[0], head[1] - 1)
            if tailcheck(head, tail) == True:
                tail = movetail(tail, head)

            


    elif direction == 'U':
        pass
    elif direction == 'L':
        pass
    elif direction == 'R':
        pass


def ans():
    head = (0, 0)
    tail = (0, 0)
    dif = [(0, 0)]
    for move in moves:
        move = move.split(" ")
        head = switch(head, move[0], move[1], tail)
    print(len(dif))

#if visited(tail, dif) == False:
     #       dif.append(tail)

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


samplehead = (4, 3)
sampletail = (6, 2)
print(movetail(sampletail, samplehead))