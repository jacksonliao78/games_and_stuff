
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d2.in') as f:
    matches = f.read().split('\n')

def win(opp, you):
    if opp == 'A' and you == 'Y':
        return 4
    elif opp == 'A' and you == 'X':
        return 3
    elif opp == 'A' and you == 'Z':
        return 8
    elif opp == 'B' and you =='Y':
        return 5
    elif opp == 'B' and you == 'X':
        return 1
    elif opp == 'B' and you == 'Z':
        return 9
    elif opp == 'C' and you == 'X':
        return 2
    elif opp == 'C' and you == 'Y':
        return 6
    elif opp == 'C' and you == 'Z':
        return 7
 

def ans():
    score = 0
    for match in matches:
        score += win(match[0], match[-1])
    print(score)

ans()