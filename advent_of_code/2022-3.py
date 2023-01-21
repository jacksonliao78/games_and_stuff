

with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d3.in') as f:
    rucksacks = f.read().split('\n')

def unpack(rucksack):
    a = int(len(rucksack) * 0.5)
    first = []
    for char in rucksack[:a]:
        first.append(char)
    for char in rucksack[a:]:
        if char in first:
            return char

def val(character):
    lower, upper= [*'abcdefghijklmnopqrstuvwxyz'], [*'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    if character.islower() == True:
        for char in lower:
            if char == character:
                return lower.index(char) + 1
    for char in upper:
        if char == character:
            return upper.index(char) + 27

def ans():
    tot = 0
    for sack in rucksacks:
        tot += val(unpack(sack))
    print(tot)

ans()
