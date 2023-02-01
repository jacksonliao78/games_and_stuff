

import heapq

with open('/Users/jliao/Code/games_and_stuff/advent_of_code/d12.in') as f:
    grid = [list(row.strip()) for row in f.readlines()]

starts = []   
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            starts.append((i, j))
        if grid[i][j] == 'E':
            en = (i, j)
        if grid[i][j] == 'a':
            starts.append((i, j))

def height(r, c):
    point = grid[r][c]
    if point == 'S':
        return 0
    elif point == 'E':
        return 25
    else:
        return ord(point) - 97

def neighbors(r, c):
    h = height(r, c)
    neighbor = []
    for add_r, add_c in ([0, 1], [0, -1], [1, 0], [-1, 0]):
        newr, newc = r + add_r, c + add_c
        if newr >= 0 and newr < len(grid) and newc >= 0 and newc < len(grid[0]):
            if height(newr, newc) <= h + 1:
                neighbor.append((newr, newc))
    return neighbor
    
def dijkstra(start, end):
    queue = []
    visited = set()
    heapq.heappush(queue, (0, start))
    while True:
        if not queue:
            break

        steps, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == end:
                return steps
            for rnew, cnew in neighbors(node[0], node[1]):
                heapq.heappush(queue, (steps + 1, (rnew, cnew)))

def ans():
    lens = []
    for start in starts:
        a = (dijkstra(start, en))
        if a is not None:
            lens.append(a)
    print(min(lens))

ans()

