

with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d9.in') as f:
    moves = f.read().split('\n')

def backcheck(front, back):
    if (((front[0]-back[0])**2)+((front[1]-back[1])**2))**0.5 >= 2:
        return True
    return False

def moveback(back, front):
    if back[0] == front[0]:
        if back[1] > front[1]:
            return (back[0], front[1]+1)
        else:   return (back[0], front[1]-1)
    elif back[1] == front[1]:
        if back[0] > front[0]:
            return (front[0]+1, back[1])
        else:   return (front[0]-1, back[1])
    elif back[0] - front[0] == 2 and back[1] - front[1] == 2:
        return (front[0] + 1, front[1] + 1)
    elif front[0] - back[0] == 2 and front[1] - back[1] == 2:
        return (front[0] - 1, front[1] - 1)
    elif back[0] - front[0] == 2 and back[1] - front[1] == -2:
        return (front[0] + 1, front[1] - 1)
    elif back[0] - front[0] == -2 and back[1] - front[1] == 2:
        return (front[0] -1, front[1] + 1)
    else:
        if front[0] - back[0] == 2:
            return (front[0] - 1, front[1])
        elif front[0] - back[0] == -2:
            return (front[0] + 1, front[1])
        elif front[1] - back[1] == 2:
            return (front[0], front[1] - 1)
        else: return (front[0], front[1] + 1)

def switch(cords, direction, amt, dif):
    if direction == 'U':
        for _ in range(int(amt)):
            cords[0] = (cords[0][0], cords[0][1] + 1)
            for i in range(9):
                if backcheck(cords[i], cords[i + 1]) == True:
                    cords[i + 1] = moveback(cords[i + 1], cords[i])
                if i == 8:
                    dif.append(cords[i + 1])        
    elif direction == 'D':
        for _ in range(int(amt)):
            cords[0] = (cords[0][0], cords[0][1] - 1)
            for i in range(9):
                if backcheck(cords[i], cords[i + 1]) == True:
                    cords[i + 1] = moveback(cords[i + 1], cords[i])
                if i == 8:
                    dif.append(cords[i + 1]) 
    elif direction == 'L':
        for _ in range(int(amt)):
            cords[0] = (cords[0][0] - 1, cords[0][1])
            for i in range(9):
                if backcheck(cords[i], cords[i + 1]) == True:
                    cords[i + 1] = moveback(cords[i + 1], cords[i])
                if i == 8:
                    dif.append(cords[i + 1])
    elif direction == 'R':
        for _ in range(int(amt)):
            cords[0] = (cords[0][0] + 1, cords[0][1])
            for i in range(9):
                if backcheck(cords[i], cords[i + 1]) == True:
                    cords[i + 1] = moveback(cords[i + 1], cords[i])
                if i == 8:
                    dif.append(cords[i + 1])
    return cords, dif


                
            


def ans():
    coords = [(0,0)] * 10
    dif = [(0,0)]
    for move in moves:
        move = move.split(" ")
        coords, dif = switch(coords, move[0], move[1], dif) 
    print(len(set(dif)))
    

ans()

