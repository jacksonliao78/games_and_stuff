
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d6.in') as f:
    msg = f.read()

def check(msg):
    alphabet = [False] * 26
    for char in msg:
        if alphabet[ord(char) - 97] == True:
            return False
        alphabet[ord(char) - 97] = True
    return True

def ans():
    start, end = 0, 4
    while True:
        if check(msg[start:end]) == True:
            print(end)
            break
        start += 1
        end += 1

ans() # -> 1760

