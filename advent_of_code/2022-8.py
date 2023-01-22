
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d8.in') as f:
    treerows = f.read().split('\n')



def le(trees, row, col):
    tree = int(trees[row][col])
    left = [*(trees[row][:col])]
    for tr in left:
        if int(tr) >= tree:
            return False
    return True
    
def ri(trees, row, col):
    tree = int(trees[row][col])
    right = [*(trees[row][col + 1:])]
    for tr in right:
        if int(tr) >= tree:
            return False
    return True

def to(trees, row, col):
    tree = int(trees[row][col])
    top = [*(''.join([trees[i][col] for i in range(row)]))]
    for tr in top:
        if int(tr) >= tree:
            return False
    return True

def bo(trees, row, col):
    tree = int(trees[row][col])
    bottom = [*(''.join([trees[i][col] for i in range(row + 1, 99)]))]
    for tr in bottom:
        if int(tr) >= tree:
            return False
    return True

def ans():
    count = 0
    t = treerows
    for i in range(0, 99):
        for j in range(0, 99):
            if bo(t, i, j) == True or to(t, i, j) == True or le(t, i, j) == True or ri(t, i, j) == True:
                count += 1
    print(count)


ans() 
#3785 too high