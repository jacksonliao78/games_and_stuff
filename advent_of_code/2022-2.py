
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d2.in') as f:
    matches = f.read().split('\n')
    
    
def win(opp, you):
    if opp == you:
        if opp == 'A':
            return 4
        elif opp == 'B':
            return 5
        elif opp == 'C':
            return 6
    elif opp == 'A' and you == 'C':
        return 3
    elif opp == 'A' and you == 'B':
        return 8
    elif opp == 'B' and you == 'C':
        return 9
    elif opp == 'B' and you == 'A':
        return 1
    elif opp == 'C' and you == 'B':
        return 2
    elif opp == 'C' and you == 'A':
        return 7
    

def ans():
    score = 0
    for match in matches:
        match = match.replace("X", "A").replace("Y", "B").replace("Z", "C")
        score += win(match[0], match[-1])
    print(score)

ans()