
with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d8.in') as f:
    treerows = f.read().split('\n')

def le(trees, row, col):
    tree = int(trees[row][col])
    left = [*(trees[row][:col])]
    count = 0
    for tr in left[::-1]:
        if int(tr) >= tree:
            return count + 1
        else: count += 1
    return count
    
    
def ri(trees, row, col):
    tree = int(trees[row][col])
    right = [*(trees[row][col + 1:])]
    count = 0
    for tr in right:
        if int(tr) >= tree:
            return count + 1
        else: count += 1
    return count
    

def to(trees, row, col):
    tree = int(trees[row][col])
    top = [*(''.join([trees[i][col] for i in range(row)]))]
    count = 0
    for tr in top[::-1]:
        if int(tr) >= tree:
            return count + 1
        else: count += 1
    return count

def bo(trees, row, col):
    tree = int(trees[row][col])
    bottom = [*(''.join([trees[i][col] for i in range(row + 1, 99)]))]
    count = 0
    for tr in bottom:
        if int(tr) >= tree:
            return count + 1
        else: count += 1
    return count

def ans():
    scenic = 0
    t = treerows
    for i in range(1, 98):
        for j in range(1, 98):
            if bo(t, i, j) * to(t, i, j) * le(t, i, j) * ri(t, i, j) > scenic:
                scenic = bo(t, i, j) * to(t, i, j) * le(t, i, j) * ri(t, i, j)   
    print(scenic)


ans() 
