

def sequence(num):
    count = 0
    highestval = [num]
    while num != 1:
        count += 1
        highestval.append(num)
        if num % 2 == 1:
            num = num * 3 + 1
        else:
            num = num / 2
    return (count, int(max(highestval)))

def ans():
    bruh, bruh1, bruh2 = [], [], []
    for i in range(1, 1001):
        bruh.append(sequence(i))
    for thing in bruh:
        bruh1.append(thing[0])
        bruh2.append(thing[1])
    print(sorted(set(bruh1))[-5:])
    print(sorted(set(bruh2))[-5:])

ans()