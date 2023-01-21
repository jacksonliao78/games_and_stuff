
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d5.in') as f:
    instructions = f.read().split('\n')
    instructions = [instruction.replace("move","").replace("from","").replace("to","").strip() for instruction in instructions[10:]]

def move(amt, start, end, crates):
    tomove = crates[start-1][(len(crates[start-1])-amt):]
    crates[start-1] = crates[start-1][:(len(crates[start-1])-amt)]
    crates[end-1].extend(tomove[::-1])
    return crates



def ans():
    crater = [['F','C','P','G','Q','R'],
['W','T','C','P'],['B','H','P','M','C'],['L','T','Q','S','M','P','R']
,['P','H','J','Z','V','G','N'],['D','P','J'],['L','G','P','Z','F','J','T','R'],
['N','L','H','C','F','P','T','J'],['G','V','Z','Q','H','T','C','W']]
    for instruction in instructions:
        instruction = instruction.split("  ")
        crater = move(int(instruction[0]), int(instruction[1]), int(instruction[2]), crater)
    msg = ''
    for row in crater:
        msg += row[-1]
    print(msg)

ans() # -> DHBJQJCCW