
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
   
unpack('vJrwpWtwJgWrhcsFMMfFFhFp')