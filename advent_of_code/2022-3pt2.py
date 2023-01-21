
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d3.in') as f:
    rucksacks = f.read().split('\n')

def val(character):
    lower, upper= [*'abcdefghijklmnopqrstuvwxyz'], [*'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    if character.islower() == True:
        for char in lower:
            if char == character:
                return lower.index(char) + 1
    for char in upper:
        if char == character:
            return upper.index(char) + 27

def unpack(r1, r2, r3):
    first, second = [], []
    for char in r1:
        first.append(char)
    for char in r2:
        if char in first:
            second.append(char)
    for char in r3:
        if char in second:
            return char

def ans():
    start, tot = 0, 0
    while start != 300:
        tot += val((unpack(rucksacks[start], rucksacks[start + 1], rucksacks[start + 2])))
        start += 3
    print(tot)

ans()
